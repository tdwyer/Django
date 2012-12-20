from django.db import models

class Homepage_Text(models.Model):
	title = models.CharField(max_length=127)
	description = models.TextField()

	def __unicode__(self):
		return self.title
