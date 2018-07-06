from channels.generic.websocket import AsyncWebsocketConsumer
import json
import logging

class ChatConsumer(AsyncWebsocketConsumer):
	"""docstring for ChatConsumer"""
	async def connect(self):
		logging.warning("connect")
		self.room_name = self.scope['url_route']['kwargs']['room_name']
		self.room_group_name = 'chat_%s' % self.room_name
		await self.channel_layer.group_add(
					self.room_group_name,
					self.channel_name
				)
		await self.accept()

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