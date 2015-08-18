from django.db import models

# Create your models here.

# Post model will have four fields: URL, Text,
# headline, and description. 
class Post(models.Model):
	url = models.CharField(max_length=200)
	text = models.CharField(max_length=200)
	headline = models.CharField(max_length=200)
	description = models.CharField(max_length=200)

	def __unicode__(self):
		return self.url