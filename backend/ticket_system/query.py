from graphene import ObjectType, Field, List, ID
from graphene_django.filter import DjangoFilterConnectionField
from graphene_django.types import DjangoObjectType
from ticket_system.core.models import Event, EventTicket, Visitor, Organization
from .types import OrganizationType, EventType, VisitorType, TicketType

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