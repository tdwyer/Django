from django import forms

class EmailForm(forms.Form):
	subject = forms.CharField(max_length=127)
	message = forms.CharField(widget=forms.Textarea(attrs={'cols': 46, 'rows': 8}))
	sender = forms.EmailField()
	recipients = forms.EmailField()