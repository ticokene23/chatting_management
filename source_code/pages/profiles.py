from django.db import models
from django.contrib.auth.models import User 
from django.utils.functional import cached_property

class Profile(models.Model):

	user = models.OneToOneField(User, on_delete=models.CASCADE)

	@cached_property
	def full_name(self):
		return "%s %s" % (self.user.last_name ,self.user.first_name) 
	