from django.db import models
from django.contrib.auth.models import User
from base_models.models import Postable

class Post(Postable):

	posted_by = models.OneToOneField(User,on_delete=models.CASCADE,blank=False, null=False)
	