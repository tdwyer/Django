from django.db import models

class Phone_Contact(models.Model):

	lable = models.CharField(max_length=40)
	number = models.CharField(max_length=12)

	def __unicode__(self):
		return self.lable