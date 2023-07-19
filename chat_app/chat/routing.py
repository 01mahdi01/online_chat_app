from django.urls import re_path
from . import consumers


WebSocket_urlpatterns = [
    re_path(r'ws/chat/(?P<room_name>\w+)/$', consumers.GamingChatConsumer.as_asgi())
]
