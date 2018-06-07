from django.db import models
from django.contrib.auth.models import User 
from ._postable import Postable
# from .posts import Post

class Comment(Postable):

	comment_by = models.OneToOneField(User,on_delete=models.CASCADE)
	for_post = models.ForeignKey('Post',on_delete=models.CASCADE, null=False, blank=False)