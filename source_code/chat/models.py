from django.db import models
from django.contrib.auth.models import User 
from django.utils.functional import cached_property
# Create your models here.

class TimeStampModel(models.Model):

	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	class Meta:
		abstract = True


class Postable(TimeStampModel):

	content = models.TextField(max_length=500, blank=False, null=True)

	class Meta:
		abstract = True

class Room(TimeStampModel):

	name = models.CharField(max_length=200, blank=True, null=True)
	participants = models.ManyToManyField(User, blank=True, null=True)

	@cached_property
	def label(self):
		return "Chat %s" % (self.name)
	

class Message(Postable):

	room = models.ForeignKey(Room, related_name='messages', on_delete=models.CASCADE)
	from_user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)

