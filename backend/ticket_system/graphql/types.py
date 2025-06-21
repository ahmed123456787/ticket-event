import graphene
from graphene import Int
from graphene_django import DjangoObjectType
from ticket_system.core.models import Event, EventTicket, EventStats, User
import django_filters


class UserFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    email = django_filters.CharFilter(lookup_expr='iexact')
    role = django_filters.CharFilter(lookup_expr='exact')
    
    class Meta:
        model = User
        fields = ['name', 'email', 'role']


class UserType(DjangoObjectType):
    class Meta:
        model = User
        filterset_class = UserFilter
        interfaces = (graphene.relay.Node,)
        fields = ('id', 'email', 'name', 'phone', 'role', 'is_active', 'date_joined')

class EventType(DjangoObjectType):
    available_tickets = Int()
    
    class Meta:
        model = Event
        fields = ('id', 'name', 'description', 'date', 'location', 'ticket_price', 
                  'nb_tickets', 'organizer', 'discount_for_tickets', 'tickets')
    
    def resolve_available_tickets(self, info):
        return self.available_tickets


class TicketType(DjangoObjectType):
    class Meta:
        model = EventTicket
        fields = ('id', 'ticket_code', 'description', 'purshased_date',
                 'updated_at', 'is_used', 'user', 'event', 'price_paid')


class EventStatsFilter(django_filters.FilterSet):
    action_type = django_filters.CharFilter(lookup_expr='exact')
    start_date = django_filters.DateTimeFilter(field_name='timestamp', lookup_expr='gte')
    end_date = django_filters.DateTimeFilter(field_name='timestamp', lookup_expr='lte')
    
    class Meta:
        model = EventStats
        fields = ['event', 'action_type', 'user']


class EventStatsType(DjangoObjectType):
    class Meta:
        model = EventStats
        filterset_class = EventStatsFilter
        interfaces = (graphene.relay.Node,)
        fields = ('id', 'event', 'action_type', 'user', 'timestamp', 'ip_address', 'user_agent', 'referrer')