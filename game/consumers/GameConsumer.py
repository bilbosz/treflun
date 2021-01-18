import json

from asgiref.sync import sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer

from game.models.Token import Token


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

        await self.move_token(data)

    @sync_to_async
    def move_token(self, data):
        token_id = int(data["id"])
        x = float(data["x"])
        y = float(data["y"])
        token = Token.objects.get(pk=token_id)
        updater = self.scope["user"]
        if token.owner.id == updater.id:
            token.x = x
            token.y = y
            token.save()
            # TODO remove later
            print("%s updated position of %s" % (updater, token.name))
            self.channel_layer.group_send(
                self.session_id,
                {
                    "type": "token_position_changed",
                    "data": data
                }
            )
        else:
            print("%s didn't update the position of %s" % (updater, token.name))

    async def token_position_changed(self, event):
        await self.send(text_data=json.dumps(event["data"]))
