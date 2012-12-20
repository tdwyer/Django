from django.conf.urls.defaults import *

urlpatterns = patterns('news.views',
	(r'^(?P<news_id>\d+)/$', 'render_news'),
	(r'^(?P<news_id>\d+)/pdf/$', 'get_news_pdf'),
	(r'^$', 'news_index'),
)