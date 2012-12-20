from header.models import HeaderImage, HccLinks, SiteLinks, HccBrownBarLinks
from job_listings.models import DegreeProgram
from news.models import News

def header(request):

	header_dict = {}
	header_dict['headerimage'] = HeaderImage.objects.get(pk=1)
	#header_dict['headerimage'] = HeaderImage.objects.all()
	header_dict['hcclinks'] = HccLinks.objects.all()
	header_dict['sitelinks'] = SiteLinks.objects.all()[::-1]
	header_dict['hccbrownbarlinks'] = HccBrownBarLinks.objects.all()
	header_dict['degreeprogram_objects'] = DegreeProgram.objects.all()
	header_dict['news_objects'] = News.objects.all().order_by('title')[:5]

	return header_dict