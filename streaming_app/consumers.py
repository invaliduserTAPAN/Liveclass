from channels.generic.websocket import AsyncWebsocketConsumer

class StreamingConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_group_name = 'live_stream'
        self.username = self.scope['user'].username

        # Add the user to the room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        # Accept the WebSocket connection
        await self.accept()

    async def disconnect(self, close_code):
        # Remove the user from the room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        # Handle received data, process and transmit the audio and video stream

        # Broadcast the received message to all users in the room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': text_data,
                'username': self.username
            }
        )

    async def chat_message(self, event):
        # Send the chat message to the WebSocket
        await self.send(text_data=event['message'])
