from django.conf.urls.defaults import *

urlpatterns = patterns('email_page.views',
	(r'^(?P<page_type>\w+)/(?P<item_id>\d+)/$', 'email_pdf'),
)