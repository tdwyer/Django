from django.conf.urls.defaults import *

from haystack.forms import ModelSearchForm
from haystack.query import SearchQuerySet
from haystack.views import SearchView, search_view_factory

sqs = SearchQuerySet()

urlpatterns = patterns('haystack.views',
		url(r'^$', search_view_factory(
			view_class=SearchView,
			template='news/search-news.html',
			searchqueryset=sqs,
			form_class=ModelSearchForm
		), name='haystack_search'),
		)