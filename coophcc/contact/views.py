from django.shortcuts import render_to_response, HttpResponseRedirect
from django.views.decorators.csrf import csrf_protect
from django.template import RequestContext
from django.core.mail import send_mail
from contact.forms import ContactForm
from contact.models import Contact

def contact(request):
	contact_list = Contact.objects.all()
	displayed_object = contact_list[0]

	if request.method == 'POST': # If the form has been submitted...
		form = ContactForm(request.POST) # A form bound to the POST data

		if form.is_valid(): # All validation rules pass
			subject = form.cleaned_data['subject']
			message = form.cleaned_data['message']
			sender = form.cleaned_data['sender']

			recipients = ['thomas@myrelay.net']
			if cc_myself:
				recipients.append(sender)

			send_mail(subject, message, sender, recipients)
			return HttpResponseRedirect('/') # Redirect after POST

	else:
		form = ContactForm() # An unbound form


	return render_to_response('contact/contact.html', {
		'displayed_object': displayed_object,
		'form': form,
		}, context_instance=RequestContext(request))