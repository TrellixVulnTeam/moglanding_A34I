from django import forms
from .models import SignUp


class SignUpForm(forms.ModelForm):
	class Meta:
		model = SignUp
		fields = ['full_name', 'email' ]

	def clean_email(self):
		email = self.cleaned_data.get('email')
		email_base, provider = email.split("@")
		domain, extension = provider.split(".")

		# Great way to validate the form for domain specific emails or extenstions etc.. #
		# if not domain == "gmail":
		# 	raise forms.ValidationError("Please a valid gmail email address")
		if not extension == "edu":
			raise forms.ValidationError("Please a valid .edu email address")
		return email

	def clean_full_name(self):
		full_name = self.cleaned_data.get('full_name')
		#could add validation code if needed here.. If not then this def is not needed and already runs in the background.
		return full_name
