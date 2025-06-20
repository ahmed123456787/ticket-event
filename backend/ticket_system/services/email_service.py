# import smtplib
# import logging
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText
# from email.mime.image import MIMEImage
# from email.utils import formatdate
# import uuid
# from django.conf import settings
# from ticket_system.core.models import EventStats, Event
# from django.template.loader import render_to_string
# from django.utils.html import strip_tags

# logger = logging.getLogger(__name__)

# class EmailService:
#     """
#     Service for sending emails with tracking capabilities for analytics.
#     """
    
#     def __init__(self, smtp_server=None, smtp_port=None, smtp_user=None, smtp_password=None):
#         self.smtp_server = smtp_server or settings.EMAIL_HOST
#         self.smtp_port = smtp_port or settings.EMAIL_PORT
#         self.smtp_user = smtp_user or settings.EMAIL_HOST_USER
#         self.smtp_password = smtp_password or settings.EMAIL_HOST_PASSWORD
#         self.from_email = settings.DEFAULT_FROM_EMAIL
    
#     def _create_tracking_pixel(self, event_id, visitor_id):
#         """
#         Create a tracking pixel URL to embed in emails.
#         This allows tracking when emails are opened.
#         """
#         tracking_id = str(uuid.uuid4())
#         tracking_url = f"{settings.BASE_URL}/api/track/email/{tracking_id}?event_id={event_id}&visitor_id={visitor_id}"
#         return tracking_url, tracking_id
    
#     def _record_email_open(self, tracking_id, event_id, visitor_id, ip_address=None, user_agent=None):
#         """
#         Record when an email is opened based on tracking pixel load.
#         """
#         try:
#             event = Event.objects.get(pk=event_id)
#             visitor = Visitor.objects.get(pk=visitor_id)
            
#             EventStats.objects.create(
#                 event=event,
#                 action_type='email_open',
#                 visitor=visitor,
#                 ip_address=ip_address,
#                 user_agent=user_agent,
#                 referrer=f"Email tracking ID: {tracking_id}"
#             )
#             return True
#         except (Event.DoesNotExist, Visitor.DoesNotExist) as e:
#             logger.error(f"Error recording email open: {str(e)}")
#             return False
    
#     def send_event_invitation(self, event, visitor, additional_context=None):
#         """
#         Send an invitation email for an event to a visitor.
#         """
#         tracking_url, tracking_id = self._create_tracking_pixel(event.id, visitor.id)
        
#         context = {
#             'event': event,
#             'visitor': visitor,
#             'tracking_url': tracking_url,
#         }
        
#         if additional_context:
#             context.update(additional_context)
        
#         # Create email content from template
#         html_content = render_to_string('emails/event_invitation.html', context)
#         text_content = strip_tags(html_content)
        
#         subject = f"You're invited to {event.name}!"
        
#         return self.send_email(
#             subject=subject,
#             message=text_content,
#             html_message=html_content,
#             recipient_list=[visitor.email],
#             tracking_data={
#                 'event_id': event.id,
#                 'visitor_id': visitor.id,
#                 'tracking_id': tracking_id
#             }
#         )
    
#     def send_ticket_confirmation(self, ticket, additional_context=None):
#         """
#         Send a ticket confirmation email.
#         """
#         event = ticket.event
#         visitor = ticket.visitor
#         tracking_url, tracking_id = self._create_tracking_pixel(event.id, visitor.id)
        
#         context = {
#             'ticket': ticket,
#             'event': event,
#             'visitor': visitor,
#             'tracking_url': tracking_url
#         }
        
#         if additional_context:
#             context.update(additional_context)
        
#         # Create email content from template
#         html_content = render_to_string('emails/ticket_confirmation.html', context)
#         text_content = strip_tags(html_content)
        
#         subject = f"Your ticket for {event.name} is confirmed!"
        
#         return self.send_email(
#             subject=subject,
#             message=text_content,
#             html_message=html_content,
#             recipient_list=[visitor.email],
#             tracking_data={
#                 'event_id': event.id,
#                 'visitor_id': visitor.id,
#                 'tracking_id': tracking_id
#             }
#         )
    
#     def send_email(self, subject, message, recipient_list, html_message=None, tracking_data=None):
#         """
#         Generic method to send an email with optional tracking.
#         """
#         try:
#             # Create message container
#             msg = MIMEMultipart('alternative')
#             msg['Subject'] = subject
#             msg['From'] = self.from_email
#             msg['To'] = ', '.join(recipient_list)
#             msg['Date'] = formatdate(localtime=True)
            
#             # Record message text
#             msg.attach(MIMEText(message, 'plain'))
            
#             if html_message:
#                 msg.attach(MIMEText(html_message, 'html'))
            
#             # Connect to server and send
#             with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
#                 if self.smtp_user and self.smtp_password:
#                     server.starttls()
#                     server.login(self.smtp_user, self.smtp_password)
#                 server.send_message(msg)
            
#             # Record stats for tracking
#             if tracking_data and 'event_id' in tracking_data and 'visitor_id' in tracking_data:
#                 try:
#                     event = Event.objects.get(pk=tracking_data['event_id'])
#                     visitor = Visitor.objects.get(pk=tracking_data['visitor_id'])
                    
#                     # Record that an email was sent
#                     EventStats.objects.create(
#                         event=event,
#                         action_type='email_sent',
#                         visitor=visitor,
#                         referrer=f"Email tracking ID: {tracking_data.get('tracking_id', 'unknown')}"
#                     )
#                 except (Event.DoesNotExist, Visitor.DoesNotExist) as e:
#                     logger.error(f"Error recording email stats: {str(e)}")
            
#             return True
#         except Exception as e:
#             logger.error(f"Error sending email: {str(e)}")
#             return False

# # Create a singleton instance for use throughout the application
# email_service = EmailService()

# def track_event_action(event, action_type, visitor=None, request=None):
#     """
#     Track various actions related to events.
    
#     Parameters:
#     - event: Event object
#     - action_type: String, one of the action types defined in EventStats.EVENT_ACTION_TYPES
#     - visitor: Optional Visitor object
#     - request: Optional HTTP request object to extract IP and user agent
#     """
#     try:
#         ip_address = None
#         user_agent = None
#         referrer = None
        
#         if request:
#             # Extract information from the request
#             x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
#             if x_forwarded_for:
#                 ip_address = x_forwarded_for.split(',')[0]
#             else:
#                 ip_address = request.META.get('REMOTE_ADDR')
                
#             user_agent = request.META.get('HTTP_USER_AGENT')
#             referrer = request.META.get('HTTP_REFERER')
        
#         # Create the stats record
#         EventStats.objects.create(
#             event=event,
#             action_type=action_type,
#             visitor=visitor,
#             ip_address=ip_address,
#             user_agent=user_agent,
#             referrer=referrer
#         )
#         return True
#     except Exception as e:
#         logger.error(f"Error tracking event action: {str(e)}")
#         return False