from channels.generic.websocket import AsyncWebsocketConsumer
from django.contrib.auth.models import AnonymousUser
from abc import ABC
import json
import logging

logger = logging.getLogger(__name__)


class MessageInterface(ABC):
    type: str
    message: str


class EventReminderMessage(MessageInterface):
    EVENT_REMINDER_TYPE = "event_reminder" 
    type = EVENT_REMINDER_TYPE
    message: str

    def __init__(self, message: str):
        self.message = message

    def __str__(self):
        return f"{self.type}: {self.message}"



class EventReminderConsumer(AsyncWebsocketConsumer):
    EVENT_REMINDER_TYPE = "event_reminder" 

    async def connect(self):
        user = self.scope['user']

        if isinstance(user, AnonymousUser):  
            logger.warning("Closing connection: user is anonymous")
            await self.close(code=1000)
            return

        eventid = self.scope['url_route']['kwargs']['eventid'] 
        logger.info(f"WebSocket connected for event: {eventid}")
        
        self.group_name = f"event_reminder_group_{eventid}"  # Use eventid to name the group
        logger.info(f"Adding to group: {self.group_name}")
        
        try:
            await self.channel_layer.group_add(
                self.group_name,
                self.channel_name
            )
            
            await self.accept()
            
            await self.send(text_data=json.dumps({
                "type": "connection_established",
                "message": f"Connected to event {eventid}"
            }))
            logger.info(f"Connection accepted for event: {eventid}")
        except Exception as e:
            logger.error(f"Error in connect: {str(e)}")
            await self.close(code=1000)


    async def disconnect(self, close_code):
        logger.info(f"WebSocket disconnected with code: {close_code}")
        if hasattr(self, 'channel_layer') and hasattr(self, 'group_name'):
            try:
                await self.channel_layer.group_discard(
                    self.group_name,
                    self.channel_name
                )
                logger.info(f"Removed from group: {self.group_name}")
            except Exception as e:
                logger.error(f"Error in disconnect: {str(e)}")


    async def receive(self, text_data=None, bytes_data=None):
        logger.info(f"Received message: {text_data}")
        try:
            text_data_json = json.loads(text_data)
            message_type = text_data_json.get("type")

            if message_type == self.EVENT_REMINDER_TYPE:  # Use the constant
                message = text_data_json.get("message")
                logger.info(f"Broadcasting message to group {self.group_name}")
                await self.channel_layer.group_send(
                    self.group_name,
                    {
                        "type": "event_reminder",  
                        "message": message
                    }
                )
        except Exception as e:
            logger.error(f"Error in receive: {str(e)}")


    async def event_reminder(self, event):
        logger.info(f"Sending event reminder to client: {event}")
        message = event["message"]
        try:
            await self.send(text_data=json.dumps({
                "type": self.EVENT_REMINDER_TYPE, 
                "message": message
            }))
            logger.info("Message sent to client successfully")
        except Exception as e:
            logger.error(f"Error sending message to client: {str(e)}")
