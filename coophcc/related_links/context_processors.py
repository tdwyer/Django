from related_links.models import Link

def link(request):

	link_dict = {}
	link_dict['link'] = Link.objects.all()

	return link_dict