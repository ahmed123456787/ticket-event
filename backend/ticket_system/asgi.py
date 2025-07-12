import os

from channels.routing import ProtocolTypeRouter
from django.core.asgi import get_asgi_application
from channels.routing import URLRouter
from ticket_system.events import routing 
from ticket_system.events.middlware import AuthenticationMiddleware

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ticket_system.settings')
django_asgi_app = get_asgi_application()

application = ProtocolTypeRouter({
    "http": django_asgi_app,
    "websocket": AuthenticationMiddleware(
        URLRouter(
            routing.websocket_urlpatterns
        )

    )
})