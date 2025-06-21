from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from ticket_system.core.models import Event, EventTicket
from ticket_system.core.permissions import IsAdminUser, IsOrganizerUser, IsVisitor
from .serializers import EventSerializer, TicketSerializer, TicketPaymentSerializer, TicketCheckInSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.decorators import action
from ticket_system.services.email_service import send_email_via_sendgrid
from ticket_system.services.qr_code import generate_ticket_image
import base64
import os
from django.conf import settings



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
        """Override to set the user when creating a ticket"""
        serializer.save(user=self.request.user)
        return super().perform_create(serializer)
        
    def list(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(serializer.data)
        
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
    

    @action(detail=False, methods=['post'], permission_classes=[IsAuthenticated, IsVisitor])
    def purchase(self, request):
        """Purchase a ticket for an event and receive QR code via email"""

        serializer = TicketPaymentSerializer(data=request.data, context={'request': request})

        if serializer.is_valid():
            ticket = serializer.save(user=request.user)  

            # Generate QR code image
            qr_buffer = generate_ticket_image(ticket)
            
            # Save QR code image to a folder
            qr_dir = os.path.join(settings.MEDIA_ROOT, 'qr_codes')
            os.makedirs(qr_dir, exist_ok=True)
            
            # Save the image file
            filename = f'ticket_{ticket.ticket_code}.png'
            file_path = os.path.join(qr_dir, filename)
            with open(file_path, 'wb') as f:
                f.write(qr_buffer.getvalue())
                    
            # Create URL for the saved image (for API response)
            qr_image_url = f'..{settings.MEDIA_URL}qr_codes/{filename}'
            print(qr_image_url)
            # Create base64 data URL (for email)
            qr_code_base64 = base64.b64encode(qr_buffer.getvalue()).decode("utf-8")
            qr_email_src = f'data:image/png;base64,{qr_code_base64}'

            # Compose and send email with embedded image
            subject = '🎫 Your Ticket Confirmation'
            html_content = f'''
                <p>Hi {request.user.name},</p>
                <p>Thank you for purchasing a ticket for <strong>{serializer.data["event"]}</strong>.</p>
                <p>Here is your ticket QR code:</p>
                <img src="cid:qr_code" alt="QR Code" style="width:200px;height:auto;" />
                <p><strong>Ticket Code:</strong> {serializer.data["ticket_code"]}</p>
                <p>Show this code at the event entrance.</p>
                <br>
                <p>Best regards,<br>Event Ticketing Team</p>
            '''

            send_email_via_sendgrid(
                to_email="zaterahmed62@gmail.com",
                subject=subject,
                html_content=html_content,
                qr_buffer=qr_buffer
            )

            # Include the QR code URL in the response
            response_data = serializer.data
            response_data['qr_code_url'] = qr_image_url
            
            return Response(response_data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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


    @action(detail=False,methods=['post'], permission_classes=[IsAuthenticated, IsOrganizerUser])
    def check_in(self,request):
        """Check the ticket using ticket code"""

        serializer = TicketCheckInSerializer(data=request.data)
        if serializer.is_valid():
            ticket = serializer.save()
            return Response({"message": "Ticket checked in successfully", "ticket_code": ticket.ticket_code}, 
                            status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)