from django.db import models

class HeaderImage(models.Model):
	banner = models.ImageField(upload_to='image')


class HccLinks(models.Model):
	name = models.CharField(max_length=54)
	url = models.CharField(max_length=127)

	def __unicode__(self):
		return self.name


class HccBrownBarLinks(models.Model):
	name = models.CharField(max_length=54)
	url = models.CharField(max_length=127)

	def __unicode__(self):
		return self.name


class SiteLinks(models.Model):
	name = models.CharField(max_length=54)
	url = models.CharField(max_length=127)

	def __unicode__(self):
		return self.name