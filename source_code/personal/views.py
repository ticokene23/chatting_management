from django.shortcuts import render
from django.views.generic import ListView
from personal.models import Profile
# Create your views here.

class UserList(ListView):

	model = Profile
	template_name = 'users/user_list.html'