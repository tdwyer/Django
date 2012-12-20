from django.db import models

class News(models.Model):
	title = models.CharField(max_length=127)
	description = models.TextField()
	created = models.DateTimeField(auto_now_add=True)
	lastedit = models.DateTimeField(auto_now=True)

	def __unicode__(self):
		return self.title

	def get_absolute_url(self):
		return '/news/' + str(self.id) + '/'