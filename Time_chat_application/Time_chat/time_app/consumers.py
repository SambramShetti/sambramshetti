# pip install channels==3.0.4
# pip install 


from channels.generic.websocket import AsyncWebsocketConsumer
import json
from asgiref.sync import sync_to_async
from django.contrib.auth.models import User
from .models import ChatRoom, ChatMessage

class ChatConsumer(AsyncWebsocketConsumer):

    async def connect(self): # this is async event so we have written async before def connect(self) and this is function definition and not function call.
        self.room_name = self.scope['url_route']['kwargs']['room_name'] # this will give room name
        self.room_group_name = 'chat_%s' % self.room_name

        # below codes are used to connect to particular room and it is a function call

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self):
        await self.channel_layer.group_discard(
            self.channel_name,
            self.room_group_name
        )

    '''
    above both the methods are used for connecting and disconnecting to web socket
    '''

    async def receive(self, text_data):
        # this is a function to receive message that user sends in room.html page.
        data = json.loads(text_data)
        message = data['message']
        username = data['username']
        room = data['room']

        await self.channel_layer.group_send(
            self.room_group_name, {
                'type':'chat_message',
                'message':message,
                'username':username,
                'room':room,
            }
        )

        await self.save_message(username, room, message) # this is save_message() function call

    async def chat_message(self, event):
    # this is function to send message to the resp chatroom or back to client.
        message = event['message']
        username = event['username']
        room = event['room']

        await self.send(text_data=json.dumps({
            'message':message,
            'username':username,
            'room':room,
        }))

    @sync_to_async # decorator is added as this is synchronous function
    def save_message(self, username, room, message):
        '''
        This method is used to store messages into db.
        '''
        user = User.objects.get(username=username)
        room = ChatRoom.objects.get(slug=room)

        ChatMessage.objects.create(user=user, room=room, message_content=message)