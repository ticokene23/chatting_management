from channels.generic.websocket import AsyncWebsocketConsumer
import json
import logging
from chat.models import Room

class ChatConsumer(AsyncWebsocketConsumer):
	"""docstring for ChatConsumer"""
	async def connect(self):
		logging.warning("connect")
		logging.warning(self.channel_name)
		try:
			self.room_name = self.scope['url_route']['kwargs']['room_name']
			room = await self._get_or_create_room(self.room_name)
			logging.warning(room)
			self.room_group_name = 'chat_%s' % self.room_name
			
			await self.channel_layer.group_add(
						self.room_group_name,
						self.channel_name
					)

			await self.accept()

		except Exception as e:
			raise e
		
    # Leave room group
	async def disconnect(self, close_code):
		logging.warning("disconnect")
		await self.channel_layer.group_discard(
			self.room_group_name, 
			self.channel_name
			)

    # Receive message from WebSocket
	async def receive(self, text_data):
		logging.warning("receive")
		logging.warning(text_data)
		text_data_json = json.loads(text_data)
		message = text_data_json['message']

		await self.channel_layer.group_send(
			self.room_group_name, {
				'type': 'chat_message',
				'message': message
			})

    # Receive message from room group
	async def chat_message(self, event):
		logging.warning("chat_message")
		message = event['message']
		await self.send(text_data=json.dumps({
			'message':message
			}))

	async def _get_or_create_room(self, room_name):
		room, ws_created = Room.objects.get_or_create(name=room_name)
		return room