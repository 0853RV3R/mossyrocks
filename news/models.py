from django.db import models
import re

# Create your models here.

class Story(models.Model):

	title = models.CharField(max_length=300)
	message = models.CharField(max_length=5000)
	date_posted = models.DateField(auto_now = True)

	def teaser(self):
                string = self.message[:200]
                condition = True
                while condition == True:
                        check = string[-1]
                        if check == " ":
                            condition = False
                        else:
                            string = string[:-1]
                return string
                


	def __unicode__(self):
		return self.title

	
class Tourdate(models.Model):

        city = models.CharField(max_length=300)
        venue = models.CharField(max_length=500)
        date = models.CharField(max_length=300)
        optional_link_1 = models.URLField(blank="True", default="")
        optional_link_1_description = models.CharField(max_length=300, blank="True", default="")
        optional_link_2 = models.URLField(blank="True", default="")
        optional_link_2_description = models.CharField(max_length=300, blank="True", default="")

        def __unicode__(self):
                return self.venue

class Contact(models.Model):

        phone = models.CharField(max_length=300)
        email = models.CharField(max_length=300)

class Sounds(models.Model):

        link = models.URLField()
        track_name = models.CharField(max_length=500)

        def __unicode__(self):
                return self.track_name
