from django import forms

class CreateAccountForm(forms.Form):
	first_name = forms.CharField(max_length=30)
	last_name = forms.CharField(max_length=30)
	username = forms.CharField(max_length=30)
	password = forms.CharField(max_length=30)
	email = forms.EmailField()


class EditProfileForm(forms.Form):
	first_name = forms.CharField(max_length=30, required=False)
	last_name = forms.CharField(max_length=30, required=False)
	email = forms.EmailField(required=False)