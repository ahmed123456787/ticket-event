from graphene import ObjectType, Field, List, ID, String, Int
from graphene_django.filter import DjangoFilterConnectionField
from ticket_system.core.models import Event, EventTicket, EventStats, User
from .types import EventType, TicketType, EventStatsType, UserType
from django.db.models import Count
from graphene import JSONString



class Query(ObjectType):
    # Regular fields
    events = List(EventType)
    event = Field(EventType, id=ID(required=True))
    tickets = List(TicketType)
    ticket = Field(TicketType, id=ID(required=True))
    users = List(UserType)
    user = Field(UserType, id=ID(required=True))
    
    # Organization-related fields (now using UserType with role filter)
    organization = Field(UserType, id=ID(required=True))
    organizations = DjangoFilterConnectionField(UserType)
    
    # Statistics fields
    event_stats = DjangoFilterConnectionField(EventStatsType)
    event_stats_summary = Field(JSONString, event_id=ID(required=True))
    event_action_counts = Field(JSONString, event_id=ID(required=True), 
                               action_type=String(), 
                               days=Int(default_value=30))

    def resolve_events(self, info):
        print(info.context.user.is_authenticated)
        return Event.objects.all()

    def resolve_event(self, info, id):
        try:
            return Event.objects.get(pk=id)
        except Event.DoesNotExist:
            return None

    def resolve_tickets(self, info):
        return EventTicket.objects.all()

    def resolve_ticket(self, info, id):
        try:
            return EventTicket.objects.get(pk=id)
        except EventTicket.DoesNotExist:
            return None
    
    def resolve_users(self, info):
        # Now we can filter by role if needed
        return User.objects.filter(role='visitor')
    
    def resolve_user(self, info, id):
        try:
            return User.objects.get(pk=id)
        except User.DoesNotExist:
            return None
    
    def resolve_organizations(self, info, **kwargs):
        # Filter users with organizer role
        return User.objects.filter(role='organizer')
    
    def resolve_organization(self, info, id):
        try:
            # Make sure we're getting a user with the organizer role
            return User.objects.get(pk=id, role='organizer')
        except User.DoesNotExist:
            return None
            
    def resolve_event_stats_summary(self, info, event_id):
        """
        Provide a summary of all stats for a specific event
        """
        try:
            # Check if event exists
            event = Event.objects.get(pk=event_id)
            
            # Get stats grouped by action type
            stats_by_action = (
                EventStats.objects
                .filter(event_id=event_id)
                .values('action_type')
                .annotate(count=Count('id'))
            )
            
            # Format as a dictionary
            result = {
                'event_id': event_id,
                'event_name': event.name,
                'stats': {item['action_type']: item['count'] for item in stats_by_action},
                'total_interactions': sum(item['count'] for item in stats_by_action)
            }
            
            return result
        except Event.DoesNotExist:
            return {'error': 'Event not found'}
            
    def resolve_event_action_counts(self, info, event_id, action_type=None, days=30):
        """
        Get time-series data of actions for visualization.
        Returns counts by day for the specified time period.
        """
        from django.utils import timezone
        from datetime import timedelta
        from django.db.models.functions import TruncDate
        
        try:
            # Define the date range
            end_date = timezone.now()
            start_date = end_date - timedelta(days=days)
            
            # Base query
            query = EventStats.objects.filter(
                event_id=event_id,
                timestamp__gte=start_date,
                timestamp__lte=end_date
            )
            
            # Filter by action type if specified
            if action_type:
                query = query.filter(action_type=action_type)
            
            # Group by date and action type
            time_series = (
                query
                .annotate(date=TruncDate('timestamp'))
                .values('date', 'action_type')
                .annotate(count=Count('id'))
                .order_by('date', 'action_type')
            )
            
            # Format results for easy consumption by frontend charts
            result = {
                'event_id': event_id,
                'period_days': days,
                'series': [
                    {
                        'date': item['date'].isoformat(),
                        'action_type': item['action_type'],
                        'count': item['count']
                    } for item in time_series
                ]
            }
            
            return result
        except Exception as e:
            return {'error': str(e)}