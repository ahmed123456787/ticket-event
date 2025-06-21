from rest_framework.serializers import Serializer 
from rest_framework import serializers




class EmailSerializer(Serializer):
    """
    Serializer for email data.
    """
    subject = serializers.CharField(max_length=255)
    body = serializers.CharField()
    recipient_email = serializers.EmailField()
    