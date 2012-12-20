from haystack.indexes import *
from haystack import site
from news.models import News


class NewsIndex(RealTimeSearchIndex):
    text = CharField(document=True, use_template=True)

    def index_queryset(self):
        """Used when the entire index for model is updated."""
        return News.objects.all()


site.register(News, NewsIndex)