from .channels import UserLoginTracker
from django.urls import path, include


websocket_urlpatterns = [
	path('users/', UserLoginTracker),
]