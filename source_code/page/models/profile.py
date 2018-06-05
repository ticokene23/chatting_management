from django.contrib.auth.models import User

class Profile(models.Model):
	user = models.OneToOneField(User)