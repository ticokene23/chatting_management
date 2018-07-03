from django.db import models
from django.contrib.auth.models import User 
from django.utils.functional import cached_property
from .base import TimeStampedModel

class Profile(TimeStampedModel):

	user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=13, blank=True, null=True)

	@cached_property
	def full_name(self):
		return "%s %s" % (self.user.last_name ,self.user.first_name) 

