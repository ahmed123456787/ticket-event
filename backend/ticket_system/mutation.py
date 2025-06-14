import graphene
from graphene import ObjectType, String, Int, ID, Field, Float, Mutation
from ticket_system.core.models import Event, EventTicket, Visitor, Organization
import uuid
from .types import EventType, VisitorType, TicketType, OrganizationType
from ticket_system.core.serializers import VisitorSerializer, EventSerializer, EventTicketSerializer, OrganizationSerializer
from django.contrib.auth import get_user_model
from datetime import datetime
from decimal import Decimal

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
            organizer = Organization.objects.get(pk=organizer_id)
        except Organization.DoesNotExist:
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
            visitor = Visitor.objects.get(pk=visitor_id)
        except Visitor.DoesNotExist:
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



class CreateVisitor(Mutation):
    class Arguments:
        name = String(required=True)
        email = String(required=True)
        phone = String()
    class Meta:
        serializer_class = VisitorSerializer 
    visitor = Field(VisitorType)
    
    def mutate(self, info, name, email, phone=None):
        visitor, created = Visitor.objects.get_or_create(
            name=name,
            email=email,
            defaults={'phone': phone}
        )
        # If visitor already exists and phone is provided, update phone if needed
        if not created and phone and visitor.phone != phone:
            visitor.phone = phone
            visitor.save()
        return CreateVisitor(visitor=visitor)


class CreateOriganization(Mutation):
    class Arguments:
        name = String(required=True)
        email = String(required=True)
        

    class Meta:
        serializer_class = OrganizationSerializer
        
    organization = Field(OrganizationType)

    def mutate(self, info, name, email,):
        organization = Organization(
            name=name,
            email=email,
        )
        organization.save()
        return CreateOriganization(organization=organization)
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
                organizer = Organization.objects.get(pk=kwargs['organizer_id'])
                event.organizer = organizer
            except Organization.DoesNotExist:
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
        serializer_class = VisitorSerializer
        
    visitor = Field(VisitorType)

    def mutate(self, info, id, **kwargs):
        try:
            visitor = Visitor.objects.get(pk=id)
        except Visitor.DoesNotExist:
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
            visitor = Visitor.objects.get(pk=id)
            visitor.delete()
            return DeleteVisitor(ok=True)
        except Visitor.DoesNotExist:
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

class Mutation(ObjectType):
    create_event = CreateEvent.Field()
    update_event = UpdateEvent.Field()
    delete_event = DeleteEvent.Field()
    create_ticket = CreateTicket.Field()
    update_ticket = UpdateTicket.Field()
    delete_ticket = DeleteTicket.Field()
    create_visitor = CreateVisitor.Field()
    update_visitor = UpdateVisitor.Field()
    delete_visitor = DeleteVisitor.Field()
    create_organization = CreateOriganization.Field()