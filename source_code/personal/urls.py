from django.urls import path
from . import views

app_name = "personal"

urlpatterns = [

	path('', views.UserList.as_view(), name="user_list"),
	path('login/', views.UserLogin.as_view(), name="user_login" ),
	path('signup/', views.UserSignUp.as_view(), name="user_signup" )
]