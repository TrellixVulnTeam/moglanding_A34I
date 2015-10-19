from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

from .forms import ContactForm
# Create your views here.


def contact(request):
	title = "Title to Contact Us"
	form = ContactForm(request.POST or None)

	context = {
		"title": title,
		"form": form,
	}

	if form.is_valid():
		# print(form.cleaned_data)
		form_email = form.cleaned_data.get("email")
		form_message = form.cleaned_data.get("message")
		form_full_name = form.cleaned_data.get("full_name")

		subject = 'MyOilGirls Contact Form'
		from_email = settings.EMAIL_HOST_USER
		contact_message = "%s: %s via %s" %(form_full_name, form_message, form_email)
		to_email = from_email
		
		send_mail(subject, contact_message, from_email, [to_email], fail_silently=False)
    		
		
		print(form_email, form_message, form_full_name)
		title = "We have been contacted"
		context = {
			"title": title,
		}

	

	return render(request, "forms.html", context)