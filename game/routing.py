from django.urls import re_path

from game.consumers.ChatConsumer import ChatConsumer
from game.consumers.GameConsumer import GameConsumer

websocket_urlpatterns = [
    re_path(r'ws/game/(?P<session_id>\d+)/$', GameConsumer),
    re_path(r'ws/chat/(?P<room_name>\w+)/$', ChatConsumer)
]
