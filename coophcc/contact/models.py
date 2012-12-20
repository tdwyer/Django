from django.db import models

class Contact(models.Model):
	title = models.CharField(max_length=127)
	post = models.TextField()

	def __unicode__(self):
		return self.title