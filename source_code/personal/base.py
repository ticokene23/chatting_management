from django.db import models

# Create your models here.

class TimeStampedModel(models.Model): 

	created_at = models.DateTimeField(auto_now_add=True) 
	updated_at = models.DateTimeField(auto_now=True) 
	
	class Meta:
		abstract = True 
 
class Postable(models.Model): 
	
	message = models.TextField(max_length=500) 

	class Meta:
		abstract =True
