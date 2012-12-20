from django.conf.urls.defaults import *

urlpatterns = patterns('',
	(r'^(?P<degree_program_id>\d+)/(?P<page_number>\d+)/$', 'job_listings.views.job_listings'),
	(r'^create_listing/$', 'job_listings.views.create_job_listing'),
	(r'^edit_listing/(?P<listing_id>\d+)/$', 'job_listings.views.edit_job_listing'),
	(r'^owners_job_listings/(?P<page_number>\d+)/$', 'job_listings.views.owners_job_listings'),
	(r'^contact_poster/(?P<degree_program_id>\d+)/(?P<job_id>\d+)/$', 'job_listings.views.contact_poster'),
	(r'^view_listing/(?P<job_id>\d+)/$','job_listings.views.view_listing'),
	(r'^view_listing/(?P<job_id>\d+)/pdf/$','job_listings.views.get_listing_pdf'),
	(r'^view_owners_listing/(?P<job_id>\d+)/$','job_listings.views.view_owners_listing'),
	(r'^delete_job_listing/(?P<job_id>\d+)/$', 'job_listings.views.delete_job_listing'),
	(r'^search/$', 'search.views.search_listings'),
	(r'^$', 'job_listings.views.job_listing_homepage'),
)