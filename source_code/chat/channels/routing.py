from django.urls import path, include
from . import consumers


websocket_urlpatterns = [
	path('ws/chat/<str:room_name>/', consumers.ChatConsumer),
]