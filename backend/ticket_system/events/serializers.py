from rest_framework.serializers import ModelSerializer 
from ticket_system.core.models import Event

class EventSerializer(ModelSerializer): 
    class Meta:
        model = Event
        fields = '__all__'  
        read_only_fields = ['id', 'created_at', 'updated_at','organizer']  