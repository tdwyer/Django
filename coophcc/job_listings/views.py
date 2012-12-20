from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response
from job_listings.models import JobListing, DegreeProgram, HomepageText
from django.contrib.auth.decorators import login_required
from job_listings.forms import JobListingForm, PosterContactForm
from django.contrib.auth.models import User
from homepage.views import render_to_pdf
from django.core.mail import send_mail


def job_listing_homepage(request):
	homepage_text_object = HomepageText.objects.all()[:1]


	return render_to_response('job_listings/jobs_homepage.html', {
		'homepage_text_object': homepage_text_object,
		}, context_instance=RequestContext(request))


def job_listings(request, degree_program_id, page_number):
	degree_program = DegreeProgram.objects.get(pk=degree_program_id)

	total_job_listings = JobListing.objects.filter(degree_program=degree_program_id)
	pages_count = total_job_listings.count()/10
	pages_count = int(pages_count)+1
	pages = []
	for i in range(pages_count):
		pages.append(i+1)

	last_listing = 10*int(page_number)
	first_listing = int(last_listing)-10
	last_listing = int(last_listing)

	try:
		job_listings = JobListing.objects.filter(degree_program=degree_program_id)[first_listing:last_listing]

	except:
		return HttpResponseRedirect('/jobs/')


	return render_to_response('job_listings/jobs.html', {
		'pages': pages,
		'job_listings': job_listings,
		'degree_program': degree_program,
		}, context_instance=RequestContext(request))


#def render_job(request, degree_program_id, job_id):
	#degreeprogram_objects = DegreeProgram.objects.all()

	#try:
		#displayed_object = JobListing.objects.get(pk=job_id)
		#degree_program = DegreeProgram.objects.get(pk=degree_program_id)
		#contact_form = PosterContactForm()

	#except:
		#return HttpResponseRedirect('/jobs/' + str(degree_program_id) + '/')


	#return render_to_response('job_listings/job_listing.html', {
		#'contact_form': contact_form,
		#'degreeprogram_objects': degreeprogram_objects,
		#'displayed_object': displayed_object,
		#'degree_program': degree_program,
		#}, context_instance=RequestContext(request))


def contact_poster(request, degree_program_id, job_id):

	if request.method == 'POST': # If the form has been submitted...
		form = PosterContactForm(request.POST) # A form bound to the POST data
		recipient = JobListing.objects.get(pk=job_id)
		recipient_email = recipient.owner.email

		if form.is_valid(): # All validation rules pass
			subject = form.cleaned_data['subject']
			message = form.cleaned_data['message']
			sender = form.cleaned_data['sender']

			recipients = [recipient_email]

			send_mail(subject, message, sender, recipients)
			return HttpResponseRedirect('/jobs/view_listing/' + ljob_id + '/') # Redirect after POST

	else:
		return HttpResponseRedirect('/jobs/view_listing/' + job_id + '/')


def view_listing(request, job_id):

	try:
		displayed_object = JobListing.objects.get(pk=job_id)
		degree_program = DegreeProgram.objects.get(pk=displayed_object.degree_program.id)
		contact_form = PosterContactForm()

	except:
		return HttpResponseRedirect('/jobs/')


	return render_to_response('job_listings/view_listing.html', {
		'contact_form': contact_form,
		'displayed_object': displayed_object,
		'degree_program': degree_program,
		}, context_instance=RequestContext(request))



@login_required(login_url='/accounts/login/')
def create_job_listing(request):
	if request.method == 'POST':
		request.POST.owner = request.user

		form = JobListingForm(request.POST)

		if form.is_valid(): # All validation rules pass

			form.save()

			return HttpResponseRedirect('/accounts/')

		else:
			return render_to_response('job_listings/create_listing.html', {
			'form': form,
			}, context_instance=RequestContext(request))


	initial = {
		'owner': request.user,
		}
	form = JobListingForm(initial)

	return render_to_response('job_listings/create_listing.html', {
		'form': form,
		}, context_instance=RequestContext(request))


@login_required(login_url='/accounts/login/')
def edit_job_listing(request, listing_id):

	if request.method == 'POST':
		request.POST.owner = request.user

		form = JobListingForm(request.POST)

		if form.is_valid(): # All validation rules pass

			job_object = JobListing.objects.get(pk=listing_id)

			degree_program = form.cleaned_data['degree_program']
			title = form.cleaned_data['title']
			description = form.cleaned_data['description']
			contact_name = form.cleaned_data['contact_name']
			contact_email = form.cleaned_data['contact_email']
			contact_phone = form.cleaned_data['contact_phone']

			job_object.degree_program = degree_program
			job_object.title = title
			job_object.description = description
			job_object.contact_name = contact_name
			job_object.contact_email = contact_email
			job_object.contact_phone = contact_phone

			job_object.save()

			return HttpResponseRedirect('/jobs/view_listing/' + listing_id + '/')

		else:
			return render_to_response('job_listings/edit_listing.html', {
			'form': form,
			}, context_instance=RequestContext(request))

	owner = request.user
	job_object = JobListing.objects.get(pk=listing_id)

	if job_object.owner == owner:

		degree_program = job_object.degree_program
		title = job_object.title
		description = job_object.description
		contact_name = job_object.contact_name
		contact_email = job_object.contact_email
		contact_phone = job_object.contact_phone

		initial = {
			'owner': owner,
			'degree_program': degree_program,
			'title': title,
			'description': description,
			'contact_name': contact_name,
			'contact_email': contact_email,
			'contact_phone': contact_phone,
			}

		form = JobListingForm(initial)
		action_url = '/jobs/edit_listing/' + str(listing_id) + '/'

	else:
		return HttpResponseRedirect('/accounts/')


	return render_to_response('job_listings/edit_listing.html', {
		'action_url': action_url,
		'job_object': job_object,
		'form': form,
		}, context_instance=RequestContext(request))


@login_required(login_url='/accounts/login/')
def owners_job_listings(request, page_number):

	total_job_listings = JobListing.objects.filter(owner=request.user)
	pages_count = total_job_listings.count()/10
	pages_count = int(pages_count)+1
	pages = []
	for i in range(pages_count):
		pages.append(i+1)

	last_listing = 10*int(page_number)
	first_listing = int(last_listing)-10
	last_listing = int(last_listing)

	try:
		job_listings = JobListing.objects.filter(owner=request.user)[first_listing:last_listing]

	except:
		job_listings = []


	return render_to_response('job_listings/owners_job_listings.html', {
		'pages': pages,
		'job_listings': job_listings,
		}, context_instance=RequestContext(request))


def view_owners_listing(request, job_id):

	try:
		displayed_object = JobListing.objects.get(owner=request.user, pk=job_id)
		degree_program = DegreeProgram.objects.get(pk=displayed_object.degree_program.id)
		contact_form = PosterContactForm()

	except:
		return HttpResponseRedirect('/jobs/owners_job_listings/1/')


	return render_to_response('job_listings/view_owners_listing.html', {
		'contact_form': contact_form,
		'displayed_object': displayed_object,
		'degree_program': degree_program,
		}, context_instance=RequestContext(request))


@login_required(login_url='/accounts/login/')
def delete_job_listing(request, job_id):
	job_listing = JobListing.objects.get(pk=job_id, owner=request.user)

	if request.method == 'POST':
		job_listing.delete()

		HttpResponseRedirect('/jobs/owners_job_listings/1/')

	try:
		displayed_object = JobListing.objects.get(pk=job_id)
		degree_program = DegreeProgram.objects.get(pk=job_listing.degree_program.id)
		contact_form = PosterContactForm()

	except:
		return HttpResponseRedirect('/jobs/owners_job_listings/1/')


	return render_to_response('job_listings/delete_job_listings.html', {
		'job_listing': job_listing,
		'contact_form': contact_form,
		'displayed_object': displayed_object,
		'degree_program': degree_program,
		}, context_instance=RequestContext(request))

#
# PDF Views
#
def get_listing_pdf(request, job_id):

	try:
		displayed_object = JobListing.objects.get(pk=job_id)
		degree_program = DegreeProgram.objects.get(pk=displayed_object.degree_program.id)
		contact_form = PosterContactForm()

	except:
		return HttpResponseRedirect('/jobs/')

	context = {
		'contact_form': contact_form,
		'displayed_object': displayed_object,
		'degree_program': degree_program,
		}

	#context = RequestContext(request, content)


	return render_to_pdf('job_listings/view_listing.html',context)