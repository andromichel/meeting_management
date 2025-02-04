from django.urls import path
from . import consumers

websocket_urlpatterns = [
    path('ws/meetings/', consumers.MeetingConsumer.as_asgi()),
]
