from django.contrib.auth.models import User

class TimeStampedModel(models.Model):
	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)

	class Meta:
		abstract = True

class Postable(TimeStampedModel):
	message = models.TextField(max_length=500)
