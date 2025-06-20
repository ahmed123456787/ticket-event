from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from ticket_system.core.models import Event, EventTicket
from ticket_system.core.permissions import IsAdminUser, IsOrganizerUser, IsVisitor
from .serializers import EventSerializer, TicketSerializer  
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404


class EventViewSet(ModelViewSet):
    """A viewset for the event model handling all CRUD operations"""

    serializer_class = EventSerializer  
    permission_classes = [IsAuthenticated] 
    authentication_classes = [JWTAuthentication] 

    def get_permissions(self):
        if self.action == 'create':
            return [IsAuthenticated(), IsOrganizerUser()]
        elif self.action in ['update', 'partial_update', 'destroy']:
            return [IsAuthenticated(), IsOrganizerUser()]  # Or add custom object-level permissions
        return [IsAuthenticated()]  # For list/retrieve etc.
    
    def get_queryset(self):
        user = self.request.user

        if not user.is_authenticated:
            return Event.objects.filter(is_published=True)

        if user.role == 'admin':
            return Event.objects.all()
        elif user.role == 'organizer':
            return Event.objects.filter(organizer=user)
        elif user.role == 'visitor':
            return Event.objects.filter(is_published=True)
        
        return Event.objects.none()
    
    def list(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(serializer.data)
   
    def perform_create(self, serializer):
        serializer.save(organizer=self.request.user)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
    

class EventTicketViewSet(ModelViewSet):
    """viewset for handling the EventTicket model"""
    
    serializer_class = TicketSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    
    def get_permissions(self):
        if self.action == 'create':
            return [IsAuthenticated(), IsVisitor()]
        elif self.action in ['update', 'partial_update', 'destroy']:
            return [IsAuthenticated(), IsAdminUser(), IsOrganizerUser()]
        return [IsAuthenticated()]
    
    def get_queryset(self):
        user = self.request.user
        
        if not user.is_authenticated:
            return EventTicket.objects.none()
            
        if user.role == 'admin':
            return EventTicket.objects.all()
        elif user.role == 'organizer':
            return EventTicket.objects.filter(event__organizer=user)
        elif user.role == 'visitor':
            return EventTicket.objects.filter(user=user)
            
        return EventTicket.objects.none()
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        
    def list(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(serializer.data)
        
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
    

    @action(detail=False, methods=['post'], permission_classes=[IsAuthenticated, IsVisitor])
    def purchase(self, request):
        event_id = request.data.get('event_id')
        quantity = int(request.data.get('quantity', 1))
        
        if not event_id:
            return Response({"error": "Event ID is required"}, status=status.HTTP_400_BAD_REQUEST)
            
        # Get the event
        event = get_object_or_404(Event, id=event_id)
        
        # Check if event has available tickets
        available_tickets = event.available_EventTickets
        if available_tickets < quantity:
            return Response(
                {"error": f"Not enough tickets available. Only {available_tickets} left."},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        # Create tickets
        tickets = []
        for _ in range(quantity):
            ticket = EventTicket.objects.create(
                event=event,
                user=request.user,
                price=event.EventTicket_price
            )
            tickets.append(ticket)
        
        # Decrease available tickets for the event
        event.available_EventTickets -= quantity
        event.save()
        
        serializer = self.get_serializer(tickets, many=True)
        
        # Add additional information to response for organizers
        response_data = {
            "tickets": serializer.data,
            "total_price": event.EventTicket_price * quantity,
            "event_name": event.name,
            "purchase_date": tickets[0].created_at if tickets else None,
        }
        
        return Response(response_data, status=status.HTTP_201_CREATED)

    @action(detail=False, methods=['get'], permission_classes=[IsAuthenticated])
    def my_tickets(self, request):
        """Get all tickets for the current user (visitor) or tickets for events organized by user (organizer)"""
        user = request.user
        
        if user.role == 'visitor':
            tickets = EventTicket.objects.filter(user=user)
        elif user.role == 'organizer':
            tickets = EventTicket.objects.filter(event__organizer=user)
        else:
            return Response({"error": "Unauthorized"}, status=status.HTTP_403_FORBIDDEN)
            
        serializer = self.get_serializer(tickets, many=True)            
        return Response(serializer.data, status=status.HTTP_200_OK)
    
        
    @action(detail=True, methods=['get'], permission_classes=[IsAuthenticated])
    def ticket_details(self, request, pk=None):
        """Get detailed information for a specific ticket"""
        ticket = self.get_object()
        
        # Check if user has permission to view this ticket
        user = request.user
        if (user.role == 'visitor' and ticket.user != user) or \
           (user.role == 'organizer' and ticket.event.organizer != user):
            return Response({"error": "You don't have permission to view this ticket"}, 
                           status=status.HTTP_403_FORBIDDEN)
        
        serializer = self.get_serializer(ticket)
        ticket_data = serializer.data
        
        # Add more detailed information
        ticket_data['event_name'] = ticket.event.name
        ticket_data['event_description'] = ticket.event.description
        ticket_data['event_date'] = ticket.event.date
        ticket_data['event_location'] = ticket.event.location
        ticket_data['purchase_date'] = ticket.created_at
        
        return Response(ticket_data)
