from django.db import models

# Create your models here.

class Story(models.Model) :

	title = models.CharField(max_length=300)
	message = models.CharField(max_length=5000)
	date_posted = models.DateField(auto_now = True)


	def __unicode__(self):
		return self.title