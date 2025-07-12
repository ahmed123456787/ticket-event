from celery import shared_task
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from .consumers import EventReminderMessage
import logging
from ticket_system.core.models import Event

logger = logging.getLogger(__name__)

@shared_task
def send_notification(type: str, message: str, eventid: str) -> int:  
    logger.info(f"Task send_notification started with type={type}, message={message}, eventid={eventid}")
    
    if type == EventReminderMessage.EVENT_REMINDER_TYPE:  

        # Send the  reminder for each event 
        events = Event.objects.all()
        for event in events:
            # fetch the users that are subscribed to the event
            for user in event.attendees.all():
                logger.info(f"User {user.name} is subscribed to event {event.name}")

            print(f"Sending event reminder: {message}")
            logger.info(f"Sending event reminder: {message}")
            
            try:
                channel_layer = get_channel_layer()
                group_name = f"event_reminder_group_{event.id}"
                channel_layer = get_channel_layer()
                logger.info(f"Sending to group: {group_name}")
                async_to_sync(channel_layer.group_send)(
                    group_name,  
                    {
                        "type": "event_reminder", 
                        "message": message
                    }
                )
                logger.info("Message sent successfully to channel layer")
                return eventid
            except Exception as e:
                logger.error(f"Error sending notification: {str(e)}")
            raise
            
    return 3