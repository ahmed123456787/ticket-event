import graphene
from graphene import ObjectType, String, Int, ID, Field, Float, Mutation
from ticket_system.core.models import Event, EventTicket, User, EventStats
import uuid
from .types import EventType, TicketType, UserType
from ticket_system.core.serializers import UserSerializer, EventSerializer, EventTicketSerializer
from django.contrib.auth import get_user_model
from datetime import datetime
from decimal import Decimal

User = get_user_model()

class CreateEvent(Mutation):
    class Arguments:
        name = String(required=True)
        description = String()
        date = String(required=False)
        location = String(required=True) 
        ticket_price = Float(required=True)
        nb_tickets = Int(required=True)
        discount_for_tickets = Float(default_value=0.0)
        organizer_id = ID(required=True)

    class Meta:
        serializer_class = EventSerializer  # Fixed typo and added proper serializer
    event = Field(EventType)

    def mutate(self, info, name, location, ticket_price, nb_tickets, organizer_id, date=datetime.now(), description=None, discount_for_tickets=0.0):
        try:
            organizer = User.objects.get(pk=organizer_id)
        except User.DoesNotExist:
            raise Exception(f"Organization with ID {organizer_id} does not exist")
            
        # Convert float values to Decimal to avoid decimal compatibility issues
        ticket_price_decimal = Decimal(str(ticket_price))
        discount_decimal = Decimal(str(discount_for_tickets))
            
        event = Event(
            name=name,
            description=description,
            date=date,
            location=location,
            ticket_price=ticket_price_decimal,
            nb_tickets=nb_tickets,
            discount_for_tickets=discount_decimal,
            organizer=organizer
        )
        event.save()
        return CreateEvent(event=event)



class CreateTicket(Mutation):
    class Arguments:
        event_id = ID(required=True)
        visitor_id = ID(required=True)
        description = String()

    class Meta:
        serializer_class = EventTicketSerializer
        
    ticket = Field(TicketType)

    def mutate(self, info, event_id, visitor_id, description=None):
        try:
            event = Event.objects.get(pk=event_id)
        except Event.DoesNotExist:
            raise Exception(f"Event with ID {event_id} does not exist")
            
        try:
            visitor = User.objects.get(pk=visitor_id)
        except User.DoesNotExist:
            raise Exception(f"Visitor with ID {visitor_id} does not exist")
            
        # Check if tickets are available
        if event.available_tickets <= 0:
            raise Exception("No tickets available for this event")
            
        # Generate unique ticket code
        ticket_code = f"{event.name[:3].upper()}-{uuid.uuid4().hex[:8].upper()}"
        
        # Calculate price (apply discount if any)
        price_paid = float(event.ticket_price) * (1 - float(event.discount_for_tickets) / 100)
        
        ticket = EventTicket(
            ticket_code=ticket_code,
            description=description or f"Ticket for {event.name}",
            visitor=visitor,
            event=event,
            price_paid=price_paid,
            is_used=False
        )
        
        ticket.save()
        return CreateTicket(ticket=ticket)



class CreateUser(Mutation):
    class Arguments:
        name = String(required=True)
        email = String(required=True)
        phone = String()
        password = String(required=True)
        role = String(default_value="visitor")
    
    class Meta:
        serializer_class = UserSerializer 
    
    user = Field(UserType)
    
    def mutate(self, info, name, email, password, role="visitor", phone=None):
        user = User(
            name=name,
            email=email,
            phone=phone,
            role=role
        )
        user.set_password(password)
        user.save()
        return CreateUser(user=user)


class UpdateUser(Mutation):
    class Arguments:
        id = ID(required=True)
        name = String()
        email = String()
        phone = String()
        role = String()
    
    class Meta:
        serializer_class = UserSerializer
        
    user = Field(UserType)

    def mutate(self, info, id, **kwargs):
        try:
            user = User.objects.get(pk=id)
        except User.DoesNotExist:
            raise Exception("User not found")
        for key, value in kwargs.items():
            if value is not None:
                setattr(user, key, value)
        user.save()
        return UpdateUser(user=user)

class DeleteUser(Mutation):
    class Arguments:
        id = ID(required=True)
    ok = graphene.Boolean()

    def mutate(self, info, id):
        try:
            user = User.objects.get(pk=id)
            user.delete()
            return DeleteUser(ok=True)
        except User.DoesNotExist:
            return DeleteUser(ok=False)

##########################################################################################

class UpdateEvent(Mutation):
    class Arguments:
        id = ID(required=True)
        name = String()
        description = String()
        date = String()
        location = String()
        ticket_price = Float()
        nb_tickets = Int()
        discount_for_tickets = Float()
        organizer_id = ID()

    class Meta:
        serializer_class = EventSerializer
        
    event = Field(EventType)

    def mutate(self, info, id, **kwargs):
        try:
            event = Event.objects.get(pk=id)
        except Event.DoesNotExist:
            raise Exception("Event not found")
        if 'organizer_id' in kwargs and kwargs['organizer_id']:
            try:
                organizer = User.objects.get(pk=kwargs['organizer_id'])
                event.organizer = organizer
            except User.DoesNotExist:
                raise Exception("Organizer not found")
        for key, value in kwargs.items():
            if key != 'organizer_id' and value is not None:
                setattr(event, key, value)
        event.save()
        return UpdateEvent(event=event)

class DeleteEvent(Mutation):
    class Arguments:
        id = ID(required=True)
    ok = graphene.Boolean()

    def mutate(self, info, id):
        try:
            event = Event.objects.get(pk=id)
            event.delete()
            return DeleteEvent(ok=True)
        except Event.DoesNotExist:
            return DeleteEvent(ok=False)

class UpdateVisitor(Mutation):
    class Arguments:
        id = ID(required=True)
        name = String()
        email = String()
        phone = String()
    class Meta:
        serializer_class = UserSerializer
        
    visitor = Field(UserType)

    def mutate(self, info, id, **kwargs):
        try:
            visitor = User.objects.get(pk=id)
        except User.DoesNotExist:
            raise Exception("Visitor not found")
        for key, value in kwargs.items():
            if value is not None:
                setattr(visitor, key, value)
        visitor.save()
        return UpdateVisitor(visitor=visitor)

class DeleteVisitor(Mutation):
    class Arguments:
        id = ID(required=True)
    ok = graphene.Boolean()

    def mutate(self, info, id):
        try:
            visitor = User.objects.get(pk=id)
            visitor.delete()
            return DeleteVisitor(ok=True)
        except User.DoesNotExist:
            return DeleteVisitor(ok=False)

class UpdateTicket(Mutation):
    class Arguments:
        id = ID(required=True)
        description = String()
        is_used = graphene.Boolean()
    class Meta:
        serializer_class = EventTicketSerializer
        
    ticket = Field(TicketType)

    def mutate(self, info, id, **kwargs):
        try:
            ticket = EventTicket.objects.get(pk=id)
        except EventTicket.DoesNotExist:
            raise Exception("Ticket not found")
        for key, value in kwargs.items():
            if value is not None:
                setattr(ticket, key, value)
        ticket.save()
        return UpdateTicket(ticket=ticket)

class DeleteTicket(Mutation):
    class Arguments:
        id = ID(required=True)
    ok = graphene.Boolean()

    def mutate(self, info, id):
        try:
            ticket = EventTicket.objects.get(pk=id)
            ticket.delete()
            return DeleteTicket(ok=True)
        except EventTicket.DoesNotExist:
            return DeleteTicket(ok=False)

class TrackEventAction(Mutation):
    class Arguments:
        event_id = ID(required=True)
        action_type = String(required=True)
        user_id = ID(required=False)
        ip_address = String(required=False)
        user_agent = String(required=False)
        referrer = String(required=False)

    success = graphene.Boolean()
    message = String()

    def mutate(self, info, event_id, action_type, user_id=None, ip_address=None, user_agent=None, referrer=None):
        try:
            # Get event
            event = Event.objects.get(pk=event_id)
            
            # Get user if provided
            user = None
            if user_id:
                try:
                    user = User.objects.get(pk=user_id)
                except User.DoesNotExist:
                    return TrackEventAction(success=False, message=f"User with ID {user_id} does not exist")
            
            # Create stats entry
            EventStats.objects.create(
                event=event,
                action_type=action_type,
                user=user,
                ip_address=ip_address,
                user_agent=user_agent,
                referrer=referrer
            )
            
            return TrackEventAction(success=True, message="Action tracked successfully")
        except Event.DoesNotExist:
            return TrackEventAction(success=False, message=f"Event with ID {event_id} does not exist")
        except Exception as e:
            return TrackEventAction(success=False, message=str(e))


class BulkTrackEventActions(Mutation):
    class Arguments:
        actions = graphene.List(graphene.JSONString, required=True)
        
    success = graphene.Boolean()
    message = String()
    tracked_count = Int()

    def mutate(self, info, actions):
        tracked_count = 0
        errors = []
        
        try:
            stats_to_create = []
            
            for action_data in actions:
                try:
                    event_id = action_data.get('event_id')
                    action_type = action_data.get('action_type')
                    user_id = action_data.get('user_id')
                    
                    # Validate required fields
                    if not event_id or not action_type:
                        errors.append(f"Missing required fields for action {tracked_count+1}")
                        continue
                    
                    # Get event
                    try:
                        event = Event.objects.get(pk=event_id)
                    except Event.DoesNotExist:
                        errors.append(f"Event with ID {event_id} does not exist")
                        continue
                    
                    # Get user if provided
                    user = None
                    if user_id:
                        try:
                            user = User.objects.get(pk=user_id)
                        except User.DoesNotExist:
                            errors.append(f"User with ID {user_id} does not exist")
                            continue
                    
                    # Create EventStats instance
                    stats_to_create.append(
                        EventStats(
                            event=event,
                            action_type=action_type,
                            user=user,
                            ip_address=action_data.get('ip_address'),
                            user_agent=action_data.get('user_agent'),
                            referrer=action_data.get('referrer')
                        )
                    )
                    tracked_count += 1
                except Exception as e:
                    errors.append(f"Error processing action {tracked_count+1}: {str(e)}")
            
            # Bulk create all valid stats objects
            if stats_to_create:
                EventStats.objects.bulk_create(stats_to_create)
            
            if errors:
                return BulkTrackEventActions(
                    success=tracked_count > 0,
                    message=f"Tracked {tracked_count} actions with {len(errors)} errors: {'; '.join(errors[:5])}" +
                            ("..." if len(errors) > 5 else ""),
                    tracked_count=tracked_count
                )
            else:
                return BulkTrackEventActions(
                    success=True,
                    message=f"Successfully tracked {tracked_count} actions",
                    tracked_count=tracked_count
                )
        except Exception as e:
            return BulkTrackEventActions(success=False, message=str(e), tracked_count=0)

class Mutation(ObjectType):
    create_event = CreateEvent.Field()
    update_event = UpdateEvent.Field()
    delete_event = DeleteEvent.Field()
    create_ticket = CreateTicket.Field()
    update_ticket = UpdateTicket.Field()
    delete_ticket = DeleteTicket.Field()
    create_user = CreateUser.Field()
    update_user = UpdateUser.Field()
    delete_user = DeleteUser.Field()
    track_event_action = TrackEventAction.Field()
    bulk_track_event_actions = BulkTrackEventActions.Field()