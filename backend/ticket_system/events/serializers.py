from rest_framework.serializers import ModelSerializer 
from ticket_system.core.models import Event, EventTicket

class EventSerializer(ModelSerializer): 
    class Meta:
        model = Event
        exclude = ['organizer']
        read_only_fields = ['id', 'created_at', 'updated_at']  


    def update(self, instance, validated_data):
        if instance.is_published:
            raise ValueError("Cannot update a published event.")
        return super().update(instance, validated_data)
    

class TicketSerializer(ModelSerializer): 
    class Meta:
        model = EventTicket
        exclude = ['user','is_used']
        read_only_fields = ['id', 'purshased_date', 'updated_at']