import json
from .mongo_client import Repo

from channels.generic.websocket import AsyncWebsocketConsumer


class ChatConsumer(AsyncWebsocketConsumer):
    count = 0

    # Connection to socket channel
    async def connect(self):
        self.room_name = "chat"
        self.room_group_name = "chat_group"
        self.user = self.scope['user']

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        ChatConsumer.count += 1
        await self.accept()
        comment = Repo.find_all("comments")
        await self.send(text_data=json.dumps({
            "connection": "Created",
            "data": json.loads(comment)
        }))

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': {
                    "connection": ChatConsumer.count
                }
            }
        )

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        # echo to client
        if text_data_json.get("comment", False):
            Repo.put("comments", {
                "comment": text_data_json.get("comment")
            })
            await self.send(text_data=json.dumps({
                "msg": "Comment created"
            }))

            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': 'chat_message',
                    'message': {
                        "comment": text_data_json.get("comment")
                    }
                }
            )
        elif text_data_json.get("delete", False):
            if text_data_json["delete"] == "all":
                if Repo.delete("comments"):
                    await self.send(text_data=json.dumps({
                        "msg": "Successfuly deleted"
                    }))

                    await self.channel_layer.group_send(
                        self.room_group_name,
                        {
                            'type': 'chat_message',
                            'message': {
                                "delete": True
                            }
                        }
                    )


        # Leave Websocket group

    async def disconnect(self, close_code):
        # Leave room group
        ChatConsumer.count -= 1
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': {
                    "connection": ChatConsumer.count
                }
            }
        )
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from room group
    async def chat_message(self, event):
        message = event['message']
        # print(message)
        # Send message to WebSocket
        await self.send(text_data=json.dumps(message))
