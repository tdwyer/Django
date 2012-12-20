from django.conf.urls.defaults import *

urlpatterns = patterns('info.views',
	(r'^(?P<info_id>\d+)/$', 'render_info'),
	(r'^(?P<info_id>\d+)/pdf/$', 'get_info_pdf'),
	(r'^$', 'info_index'),
)