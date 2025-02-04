import os
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
import secretary.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'meeting_management.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            secretary.routing.websocket_urlpatterns
        )
    ),
})
