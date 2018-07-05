from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout
from django.views.generic import ListView, View
from personal.models import Profile
import logging
# Create your views here.
class HelloView(View):

	def get(self, request, name="World"):
		return HttpResponse("Hello {}!".format(name))


class UserLogin(View):

	def get(self, request):
		form = AuthenticationForm()
		if request.method == 'POST':
			form = AuthenticationForm(data=request.POST)
			if form.is_valid():
				form.save()
				login(request, form.get_user())
				return redirect(reverse('personal:user_list'))
			else:
				print(form.errors)

		return render(request, 'users/login.html', { 'form': form })


class UserSignUp(View):

	def get(self, request):
		form = UserCreationForm()
		if request.method == 'POST':
			form = UserCreationForm(data=request.POST)
			if form.is_valid():
				login(request, form.get_user())
				return redirect(reverse('personal:user_list'))
			else:
				print(form.errors)

		return render(request, 'users/signup.html', {'form': form})

class UserList(ListView):

	model = Profile
	template_name = 'users/user_list.html'