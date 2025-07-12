from .models import Event, EventTicket, EventStats, User
from rest_framework.serializers import ModelSerializer



class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'name', 'email', 'phone', 'role', 'is_active')
        read_only_fields = ('id', 'date_joined')


class EventSerializer(ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'
        read_only_fields = ('id', 'organizer', 'attendees')

    def create(self, validated_data):
        event = Event.objects.create(**validated_data)
        return event

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.date = validated_data.get('date', instance.date)
        instance.location = validated_data.get('location', instance.location)
        instance.nb_tickets = validated_data.get('nb_tickets', instance.nb_tickets)
        instance.description = validated_data.get('description', instance.description)
        instance.discount_for_tickets = validated_data.get('discount_for_tickets', instance.discount_for_tickets)
        instance.ticket_price = validated_data.get('ticket_price', instance.ticket_price)
        instance.save()
        return instance
    

class EventTicketSerializer(ModelSerializer):
    class Meta:
        model = EventTicket
        fields = '__all__'
        read_only_fields = ('id', 'event', 'user')

    def create(self, validated_data):
        ticket = EventTicket.objects.create(**validated_data)
        return ticket

    def update(self, instance, validated_data):
        instance.event = validated_data.get('event', instance.event)
        instance.user = validated_data.get('user', instance.user)
        instance.save()
        return instance


class EventStatsSerializer(ModelSerializer):
    class Meta:
        model = EventStats
        fields = '__all__'
        read_only_fields = ('id', 'timestamp')