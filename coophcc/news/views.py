from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response
from news.models import News
from homepage.views import render_to_pdf
from django.core.mail import EmailMessage
from email_page.forms import EmailForm


def news_index(request):
	news_objects = News.objects.all().order_by('title')[:1]

	displayed_object = news_objects[0]


	return render_to_response('news/news-homepage.html', {
		'displayed_object': displayed_object,
		}, context_instance=RequestContext(request))


def render_news(request, news_id):

	try:
		displayed_object = News.objects.get(pk=news_id)

	except:
		return HttpResponseRedirect('/news/')


	return render_to_response('news/news.html', {
		'displayed_object': displayed_object,
		}, context_instance=RequestContext(request))

#
# PDF Views
#
def get_news_pdf(request, news_id):

	try:
		displayed_object = News.objects.get(pk=news_id)

	except:
		return HttpResponseRedirect('/news/')


	context = {
		'displayed_object': displayed_object,
		}

	#context = RequestContext(request, context)


	return render_to_pdf('news/news.html', context)
