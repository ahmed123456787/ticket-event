from rest_framework.serializers import ModelSerializer 
from ticket_system.core.models import Event, EventTicket
from django.utils import timezone
from rest_framework import serializers

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
    event = serializers.PrimaryKeyRelatedField(queryset=Event.objects.all())

    class Meta:
        model = EventTicket
        exclude = ['user','is_used','check_in_date', 'qr_code_image']
        read_only_fields = ['id', 'purshased_date', 'updated_at','ticket_code']


    def create(self, validated_data):
        # Get the event ID from the request data
        event_id = validated_data.get('event').id

        print(event_id)
        try:
            event = Event.objects.get(id=event_id)
            # check if the user has already purchased a ticket for this event
            if EventTicket.objects.filter(event=event, user=self.context['request'].user).exists():
                raise serializers.ValidationError({
                    "non_field_errors": ["You have already purchased a ticket for this event."]
                })
            import uuid
            ticket_code = str(uuid.uuid4())[:8].upper()
            validated_data['ticket_code'] = ticket_code

            # Update the event object directly
            event.nb_tickets -= 1
            event.save()

            validated_data['event'] = event
            validated_data['user'] = self.context['request'].user
            return super().create(validated_data)
        
        except Event.DoesNotExist:
            raise ValueError("Event with the provided ID does not exist.")


class TicketPaymentSerializer(ModelSerializer): 
    event = serializers.PrimaryKeyRelatedField(queryset=Event.objects.filter(is_published=True))

    class Meta:
        model = EventTicket
        fields = ['event', 'price_paid', 'ticket_code']
        read_only_fields = ['ticket_code']

    def validate(self, attrs):
        event = attrs.get('event')

        if event.is_published is False:
            raise ValueError("Cannot purchase tickets for unpublished events.")
        if not event:
            raise ValueError("Event must be provided.")
        if event.available_tickets <= 0:
            raise ValueError("No available tickets for this event.")
        if event.date > timezone.now():
            raise ValueError("Cannot purchase tickets for events that have not started yet.")
        return attrs


    def create(self, validated_data):
        event = validated_data.get('event')

        # Find an existing ticket for the user and event
        try:
            ticket = EventTicket.objects.get(event=event, user=self.context['request'].user)
        except EventTicket.DoesNotExist:
            raise ValueError("No ticket found for the user and event.")

        # Reduce ticket count
        event.nb_tickets -= 1
        event.save()

        ticket.price_paid = validated_data.get('price_paid', ticket.price_paid)
        ticket.save()

        return ticket
    


class TicketCheckInSerializer(serializers.Serializer):
    ticket_code = serializers.CharField()

    def validate(self, attrs):
        ticket_code = attrs.get('ticket_code')
        if not ticket_code:
            raise serializers.ValidationError("Ticket code must be provided for check-in.")
        
        try:
            ticket = EventTicket.objects.get(ticket_code=ticket_code, is_used=False, is_purshased=True)
        except EventTicket.DoesNotExist:
            raise serializers.ValidationError("Invalid or already used ticket code or ticket not purchased.")
        
        if ticket.event.date > timezone.now():
            raise serializers.ValidationError("Cannot check in for events that haven't started yet.")

        attrs['ticket'] = ticket
        return attrs
