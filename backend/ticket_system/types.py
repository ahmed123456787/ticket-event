import graphene
from graphene import  Int
from graphene_django import DjangoObjectType
from ticket_system.core.models import Event, EventTicket, Visitor, Organization
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
        fields = ("id", "name", "email","password" "phone", "address", "created_at", "updated_at")  # Add all relevant fields

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