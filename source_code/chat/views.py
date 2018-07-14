from django.shortcuts import render
from django.utils.safestring import mark_safe
from django.views import View
from chat.models import Room
import json
import logging
# Create your views here.


class RoomList(View):

	def get(self, request, *args, **kwargs):
		room_list = Room.objects.all()
		logging.warning(room_list)
		
		return render(request, 'chat/index.html', {
			'room_list': room_list
			})


class RoomDetail(View):

	def get(self, request, *args, **kwargs):
		room_name = kwargs.get('room_name')

		return render(request, 'chat/room.html', {
			'room_name_json': mark_safe(json.dumps(room_name))
		})		


