from django.db import models
from django.contrib.auth.models import User

class HomepageText(models.Model):
	description = models.TextField()

	def __unicode__(self):
		return self.description


class DegreeProgram(models.Model):
	title = models.CharField(max_length=127)

	def __unicode__(self):
		return self.title

	def get_absolute_url(self):
		return '/jobs/' + str(self.id) + '/'


class JobListing(models.Model):
	degree_program = models.ForeignKey('DegreeProgram')
	owner = models.ForeignKey(User)
	title = models.CharField(max_length=127)
	description = models.TextField()
	contact_name = models.CharField(max_length=53, blank=True)
	contact_email = models.EmailField(blank=True)
	contact_phone = models.CharField(max_length=14, blank=True)
	created = models.DateTimeField(auto_now_add=True)
	lastedit = models.DateTimeField(auto_now=True)

	def __unicode__(self):
		return self.title

	def get_absolute_url(self):
		return '/jobs/view_listing/'+ str(self.id) + '/'