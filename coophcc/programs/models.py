from django.db import models

class Program(models.Model):
	title = models.CharField(max_length=127)
	url = models.URLField()


	def __unicode__(self):
		return self.title


class AdditionalLinks(models.Model):
	name = models.CharField(max_length=54)
	url = models.URLField()

	def __unicode__(self):
		return self.name