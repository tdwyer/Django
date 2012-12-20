from django.conf.urls.defaults import *

urlpatterns = patterns('search.views',
	(r'^hcc_search/$', 'hcc_search'),
	)