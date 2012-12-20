from haystack.indexes import *
from haystack import site
from job_listings.models import JobListing



class JobListingIndex(RealTimeSearchIndex):
	text = CharField(document=True, use_template=True)


	def index_queryset(self):
		"""Used when the entire index for model is updated."""
		return JobListing.objects.all()


site.register(JobListing, JobListingIndex)