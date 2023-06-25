from django.urls import re_path
from streaming_app.consumers import StreamingConsumer

websocket_urlpatterns = [
    re_path(r'ws/streaming/$', StreamingConsumer.as_asgi()),
]
