from django.db import models

class Link(models.Model):
	name = models.CharField(max_length=40)
	url = models.URLField()

	def __unicode__(self):
		return self.name