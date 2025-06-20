from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from ticket_system.core.models import Event
from ticket_system.core.permissions import IsAdminUser, IsOrganizerUser, IsVisitor
from .serializers import EventSerializer  
from rest_framework_simplejwt.authentication import JWTAuthentication


class EventViewSet(ModelViewSet):
    """A viewset for the event model """

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
        print(serializer.data)
        return Response(serializer.data)
   
    def perform_create(self, serializer):
        serializer.save(organizer=self.request.user)

   