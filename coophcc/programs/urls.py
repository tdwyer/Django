from django.conf.urls.defaults import *

urlpatterns = patterns('programs.views',
	(r'^$', 'program_list'),
)