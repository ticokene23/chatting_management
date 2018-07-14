from django.urls import path
from . import views

app_name = "chat"

urlpatterns = [

	path('',  views.RoomList.as_view(), name='index'),
	path('<str:room_name>/', views.RoomDetail.as_view(), name="room")
]