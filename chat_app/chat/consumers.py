import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync


class GamingChatConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = "chat_%s" % self.room_name
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        self.accept()

    def receive(self, text_data=None):
        json_text_data = json.loads(text_data)
        message = json_text_data["message"]
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {"type": "chat_message", "message": message}
        )

    def chat_message(self, event):
        message = event["message"]
        self.send(text_data=json.dumps(
            {
                "type": "chat",
                "message": message
            }
        ))
