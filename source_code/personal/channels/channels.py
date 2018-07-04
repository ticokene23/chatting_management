from channels.generic.websocket import AsyncWebsocketConsumer
import json
import logging

class UserLoginTracker(AsyncWebsocketConsumer):
	async def connect(self):
		logging.warning("connect")
		await self.accept()

	async def disconnect(self, message):
		logging.warning("disconnect")

	async def receive(self, text_data):
		logging.warning(text_data)
	 