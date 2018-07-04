from django.conf.urls import url
from . import views

app_name = "personal"

urlpatterns = [

	url(r'^$', views.UserList.as_view(), name="user_list"),
]