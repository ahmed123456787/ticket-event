import graphene
from graphene import ObjectType, String, Int, List, ID, Field, Float, Mutation
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from ticket_system.core.models import Event, EventTicket, Visitor, Organization
import uuid
import django_filters


class OrganizationFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    email = django_filters.CharFilter(lookup_expr='iexact')
    
    class Meta:
        model = Organization
        fields = ['name', 'email']


class OrganizationType(DjangoObjectType):
    class Meta:
        model = Organization
        filterset_class = OrganizationFilter
        interfaces = (graphene.relay.Node,)
        fields = ("id", "name", "email", "phone", "address", "created_at", "updated_at")  # Add all relevant fields

class EventType(DjangoObjectType):
    available_tickets = Int()
    
    class Meta:
        model = Event
        fields = ('id', 'name', 'description', 'date', 'location', 'ticket_price', 
                  'nb_tickets', 'organizer', 'discount_for_tickets', 'tickets')
    
    def resolve_available_tickets(self, info):
        return self.available_tickets


class VisitorType(DjangoObjectType):
    class Meta:
        model = Visitor
        fields = ('id', 'name', 'email', 'phone', 'tickets')



class TicketType(DjangoObjectType):
    class Meta:
        model = EventTicket
        fields = ('id', 'ticket_code', 'description', 'purshased_date',
                 'updated_at', 'is_used', 'visitor', 'event', 'price_paid')


class Query(ObjectType):
    # Regular fields
    events = List(EventType)
    event = Field(EventType, id=ID(required=True))
    tickets = List(TicketType)
    ticket = Field(TicketType, id=ID(required=True))
    visitors = List(VisitorType)
    visitor = Field(VisitorType, id=ID(required=True))
    
    # Organization fields with filtering
    organization = Field(OrganizationType, id=ID(required=True))
    # Use DjangoFilterConnectionField for filtered connections
    organizations = DjangoFilterConnectionField(OrganizationType)

    def resolve_events(self, info):
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
    
    def resolve_visitors(self, info):
        return Visitor.objects.all()
    
    def resolve_visitor(self, info, id):
        try:
            return Visitor.objects.get(pk=id)
        except Visitor.DoesNotExist:
            return None
    
    def resolve_organizations(self, info, **kwargs):
        # The filtering is now handled by the DjangoFilterConnectionField
        return Organization.objects.all()
    
    def resolve_organization(self, info, id):
        try:
            return Organization.objects.get(pk=id)
        except Organization.DoesNotExist:
            return None

##########################################################################################

class CreateEvent(Mutation):
    class Arguments:
        name = String(required=True)
        description = String()
        date = String(required=True)
        location = String(required=True) 
        ticket_price = Float(required=True)
        nb_tickets = Int(required=True)
        discount_for_tickets = Float(default_value=0.0)
        organizer_id = ID(required=True)

    event = Field(EventType)

    def mutate(self, info, name, date, location, ticket_price, nb_tickets, organizer_id, description=None, discount_for_tickets=0.0):
        try:
            organizer = Organization.objects.get(pk=organizer_id)
        except Organization.DoesNotExist:
            raise Exception(f"Organization with ID {organizer_id} does not exist")
            
        event = Event(
            name=name,
            description=description,
            date=date,
            location=location,
            ticket_price=ticket_price,
            nb_tickets=nb_tickets,
            discount_for_tickets=discount_for_tickets,
            organizer=organizer
        )
        event.save()
        return CreateEvent(event=event)



class CreateTicket(Mutation):
    class Arguments:
        event_id = ID(required=True)
        visitor_id = ID(required=True)
        description = String()

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
        
    visitor = Field(VisitorType)
    
    def mutate(self, info, name, email, phone=None):
        visitor = Visitor(
            name=name,
            email=email,
            phone=phone
        )
        visitor.save()
        return CreateVisitor(visitor=visitor)

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

# Create Schema
schema = graphene.Schema(query=Query, mutation=Mutation)