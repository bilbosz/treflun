import json

from asgiref.sync import sync_to_async, async_to_sync
from channels.generic.websocket import AsyncWebsocketConsumer, WebsocketConsumer

from . import models


class GameConsumer(AsyncWebsocketConsumer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.session_id = None

    async def connect(self):
        self.session_id = self.scope["url_route"]["kwargs"]["session_id"]
        await self.channel_layer.group_add(
            self.session_id,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, code):
        await self.channel_layer.group_discard(
            self.session_id,
            self.channel_name
        )

    async def receive(self, text_data=None, bytes_data=None):
        data = json.loads(text_data)
        token_id = int(data["id"])
        x = float(data["x"])
        y = float(data["y"])
        await self.move_token(token_id, x, y)

        await self.channel_layer.group_send(
            self.session_id,
            {
                "type": "token_position_changed",
                "data": data
            }
        )

    @sync_to_async
    def move_token(self, id, x, y):
        token = models.Token.objects.get(pk=id)
        token.x = x
        token.y = y
        token.save()

    async def token_position_changed(self, event):
        await self.send(text_data=json.dumps(event["data"]))


class ChatConsumer(WebsocketConsumer):
    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)
        self.room_name = kwargs["room_name"]
        self.room_group_name = "chat_{self.room_name}"

    def connect(self):
        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                "type": "chat_message",
                "message": message,
                "sender": self.scope["user"].username
            }
        )

    # Receive message from room group
    def chat_message(self, event):
        message = event["message"]
        sender = event["sender"]

        # Send message to WebSocket
        self.send(text_data=json.dumps({
            "message": message,
            "sender": sender
        }))
