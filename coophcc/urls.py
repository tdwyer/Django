from django.conf.urls.defaults import patterns, include, url
from django.conf.urls.defaults import *


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	(r'^admin/', include(admin.site.urls)),
	(r'^contact/', include('contact.urls')),
	(r'^info/', include('info.urls')),
	(r'^news/search/', include('news.search-urls')),
	(r'^news/', include('news.urls')),
	(r'^programs/', include('programs.urls')),
	(r'^jobs/search/', include('job_listings.search-urls')),
	(r'^jobs/', include('job_listings.urls')),
	(r'^accounts/', include('user_management.urls')),
	(r'^search/', include('search.urls')),
	(r'^contact/', include('contact.urls')),
	(r'^email_page/', include('email_page.urls')),
	(r'^$', 'homepage.views.homepage'),
)