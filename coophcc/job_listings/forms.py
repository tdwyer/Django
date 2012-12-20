from django.forms import ModelForm, HiddenInput, TextInput, Textarea, CharField
from job_listings.models import JobListing
from django import forms

class JobListingForm(ModelForm):
	title = CharField(max_length=127, widget=TextInput(attrs={'size':'75'}))

	class Meta:
		model = JobListing
		widgets = {
			'owner': HiddenInput(),
			'description': Textarea(attrs={'cols': 90, 'rows': 20}),
		}


class PosterContactForm(forms.Form):
    subject = forms.CharField(max_length=127)
    message = forms.CharField(widget=forms.Textarea(attrs={'cols': 46, 'rows': 8}))
    sender = forms.EmailField()