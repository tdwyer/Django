from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response
from homepage.models import Homepage_Text
from news.models import News
from job_listings.models import JobListing
from info.models import Info


#
# PDF Redering
import cStringIO as StringIO
import xhtml2pdf.pisa as pisa
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
from cgi import escape


def render_to_pdf(template_src, context_dict):
    template = get_template(template_src)
    context = Context(context_dict)
    html  = template.render(context)
    result = StringIO.StringIO()

    pdf = pisa.pisaDocument(StringIO.StringIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), mimetype='application/pdf')
    return HttpResponse('We had some errors<pre>%s</pre>' % escape(html))

#
#


def homepage(request):
	homepage_text = Homepage_Text.objects.all()[:1]
	news_objects = News.objects.all()[:3]
	info_objects = Info.objects.all()
	job_objects = JobListing.objects.all()[:3]


	return render_to_response('homepage.html', {
		'homepage_text': homepage_text,
		'news_objects': news_objects,
		'info_objects': info_objects,
		'job_objects': job_objects,
		}, context_instance=RequestContext(request))