from django.urls import re_path

from ticket_system.events.consumers import EventReminderConsumer



websocket_urlpatterns = [
    re_path(r'ws/events/(?P<eventid>\d+)/$', EventReminderConsumer.as_asgi()),
]