from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response
from programs.models import Program, AdditionalLinks

def program_list(request):
	additional_links = AdditionalLinks.objects.all().order_by('name')
	program_objects = Program.objects.all().order_by('title')


	return render_to_response('programs/programs.html', {
		'additional_links': additional_links,
		'program_objects': program_objects,
		}, context_instance=RequestContext(request))