from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
import json
import logging

class ChatConsumer(WebsocketConsumer):
	"""docstring for ChatConsumer"""
	async def connect(self):
		logging.warning("connect")
		self.room_name = self.scope['url_route']['kwargs']['room_name']
		self.room_group_name = 'chat_%s' % self.room_name
		async_to_sync(self.channel_layer.group_add)(
					self.room_group_name,
					self.channel_name
				)
		self.accept()

    # Leave room group
	def disconnect(self, close_code):
		logging.warning("disconnect")
		async_to_sync(self.channel_layer.group_discard)(
			self.room_group_name, 
			self.channel_name
			)

    # Receive message from WebSocket
	def receive(self, text_data):
		logging.warning("receive")
		text_data_json = json.loads(text_data)
		message = text_data_json['message']

		self.send(text_data=json.dumps({
				'message': message
			}))

		async_to_sync(self.channel_layer.group_send)(
			self.room_group_name, {
				'type': 'chat_message',
				'message': message
			})

    # Receive message from room group
	def chat_message(self, event):
		logging.warning("chat_message")
		message = event['message']
		self.send(text_data=json.dumps({
			'message':message
			}))