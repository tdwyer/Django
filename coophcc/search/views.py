from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response
from job_listings.models import JobListing, DegreeProgram, HomepageText
from search.forms import JobSearchForm

def hcc_search(request):

	if request.method == 'POST':
		q = request.POST['q']

		return HttpResponseRedirect('http://www2.honolulu.hawaii.edu/?q=search/node/' + q)

	return HttpResponseRedirect('/')


def search_listings(request):
	degree_programs = DegreeProgram.objects.all()
	homepage_text_object = HomepageText.objects.all()[:1]

	form = JobSearchForm()

	return render_to_response('search/job_search.html', {
		'homepage_text_object': homepage_text_object,
		'form': form,
		}, context_instance=RequestContext(request))