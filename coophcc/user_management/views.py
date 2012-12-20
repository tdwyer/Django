from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.auth.models import User, Group
#from django.contrib.auth import authenticate, login, logout
from user_management.forms import CreateAccountForm, EditProfileForm
from django.contrib.auth.decorators import login_required
from job_listings.models import JobListing


def create_account(request):
	error = ''

	if request.method == 'POST':

		form = CreateAccountForm(request.POST)

		if form.is_valid(): # All validation rules pass

			first_name = form.cleaned_data['first_name']
			last_name = form.cleaned_data['last_name']
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			email = form.cleaned_data['email']

			try:
				username_taken = User.objects.get(username=username)
				error = 'Username Taken'

				return render_to_response('user_management/create_account.html', {
					'error': error,
					'form': form,
					}, context_instance=RequestContext(request))

			except:
				try:
					email_taken = User.objects.get(email=email)
					error = 'E-mail Taken'

					return render_to_response('user_management/create_account.html', {
						'error': error,
						'form': form,
						}, context_instance=RequestContext(request))

				except:

					user = User.objects.create_user(username, email, password)

					newuser = User.objects.get(username=username)

					JobPoster = Group.objects.get(name='JobPoster')

					newuser.first_name = first_name
					newuser.last_name = last_name
					newuser.groups.add(JobPoster)
					newuser.save()

					return HttpResponseRedirect('/accounts/')

	form = CreateAccountForm()

	return render_to_response('user_management/create_account.html', {
	'error': error,
	'form': form,
	}, context_instance=RequestContext(request))


@login_required(login_url='/accounts/login/')
def edit_profile(request):
	error = ''

	if request.method == 'POST':

		form = EditProfileForm(request.POST)

		if form.is_valid(): # All validation rules pass

			first_name = form.cleaned_data['first_name']
			last_name = form.cleaned_data['last_name']
			email = form.cleaned_data['email']

			user = User.objects.get(username=request.user)
			user.first_name = first_name
			user.last_name = last_name
			user.email = email
			user.save()

			return HttpResponseRedirect('/accounts/')

		return HttpResponseRedirect('/accounts/edit_profile/')

	user = request.user

	initial = {
		'first_name': user.first_name,
		'last_name': user.last_name,
		'email': user.email,
		}


	form = EditProfileForm(initial)

	return render_to_response('user_management/edit_profile.html', {
		'error': error,
		'form': form,
		}, context_instance=RequestContext(request))


@login_required(login_url='/accounts/login/')
def profile(request):
	user = request.user

	users_listings = JobListing.objects.filter(owner=user)
	total_listings = users_listings.count()


	return render_to_response('user_management/profile.html', {
		'user': user,
		'total_listings': total_listings,
		}, context_instance=RequestContext(request))