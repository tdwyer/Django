from django.shortcuts import render_to_response, HttpResponseRedirect
from django.views.decorators.csrf import csrf_protect
from django.template import RequestContext
from email_page.forms import EmailForm
from django.core.mail import EmailMessage
from news.views import get_news_pdf
from job_listings.views import get_listing_pdf


def email_pdf(request, page_type, item_id):

	if request.method == 'POST': # If the form has been submitted...
		form = EmailForm(request.POST) # A form bound to the POST data

		if form.is_valid(): # All validation rules pass
			subject = form.cleaned_data['subject']
			message = form.cleaned_data['message']
			sender = form.cleaned_data['sender']
			recipients = form.cleaned_data['recipients']

			if page_type == 'news':
				attachment = get_news_pdf(request, item_id)
			elif page_type == 'jobs':
				attachment = get_listing_pdf(request, item_id)
			elif page_type == 'info':
				attachment = get_info_pdf(request, item_id)

			email = EmailMessage(subject, message, sender, [recipients])
			email.attach('attachment', attachment, 'application/pdf')
			email.send()

			if page_type == 'news':
				return HttpResponseRedirect('/news/' + str(news_id) + '/') # Redirect after POST
			elif page_type == 'jobs':
				return HttpResponseRedirect('/jobs/view_listing/' + str(news_id) + '/') # Redirect after POST
			elif page_type == 'info':
				return HttpResponseRedirect('/info/' + str(news_id) + '/') # Redirect after POST

	else:
		form = EmailForm() # An unbound form

	form = EmailForm()

	return render_to_response('email_page/email_pdf.html', {
		'page_type': page_type,
		'item_id': item_id,
		'form': form,
		}, context_instance=RequestContext(request))