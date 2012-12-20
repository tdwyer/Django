from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response
from info.models import Info
from homepage.views import render_to_pdf


def info_index(request):
	info_objects = Info.objects.all().order_by('title')

	displayed_object = info_objects[0]


	return render_to_response('info/info.html', {
		'info_objects': info_objects,
		'displayed_object': displayed_object,
		}, context_instance=RequestContext(request))


def render_info(request, info_id):
	info_objects = Info.objects.all().order_by('title')

	try:
		displayed_object = Info.objects.get(pk=info_id)

	except:
		return HttpResponseRedirect('/info/')


	return render_to_response('info/info.html', {
		'info_objects': info_objects,
		'displayed_object': displayed_object,
		}, context_instance=RequestContext(request))


#
# PDF Veiws
#
def get_info_pdf(request, info_id):
	info_objects = Info.objects.all().order_by('title')

	try:
		displayed_object = Info.objects.get(pk=info_id)

	except:
		return HttpResponseRedirect('/info/')

	context = {
		'info_objects': info_objects,
		'displayed_object': displayed_object,
		}

	#context = RequestContext(request, content)


	return render_to_pdf('info/info.html', context)