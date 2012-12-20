from security_widget.models import Phone_Contact

def phone_contact(request):

	phone_contact_dict = {}
	phone_contact_dict['phone_contact'] = Phone_Contact.objects.all()

	return phone_contact_dict