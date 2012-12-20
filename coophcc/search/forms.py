from django.forms import ModelForm, HiddenInput, TextInput, Textarea, CharField, Select
from django import forms
from job_listings.models import DegreeProgram

JOB_SEARCH_CHOICES = [
	['1','one',],
	['1', 'two',],
	['3', 'three',]
	]

class JobSearchForm(forms.Form):

	program = forms.ChoiceField(widget=Select(), choices=JOB_SEARCH_CHOICES)
	q = forms.CharField(label='Search', max_length=127, widget=TextInput(attrs={'size':'75'}))
