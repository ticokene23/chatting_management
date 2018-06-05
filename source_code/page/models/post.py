from postable import Postable
from django.contrib.auth.models import User

class Post(Postable):
	posted_by = models.OneToOne(User)
	