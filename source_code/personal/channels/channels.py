from channels.generic.websocket import AsyncWebsocketConsumer, WebsocketConsumer
from channels.auth import login
import json
import logging

class UserLoginTracker(WebsocketConsumer):
	groups=['users']

	def connect(self):
		logging.warning("connect")
		self.accept()

	def disconnect(self, message):
		logging.warning("disconnect")

	def receive(self, text_data):
		# async_to_sync(login)(self.scope, user)
		# self.scope["session"].save()
		async_to_sync(login)(self.scope, user)
		self.scope["session"].save()
		logging.warning("receive")
		logging.warning(text_data)
        