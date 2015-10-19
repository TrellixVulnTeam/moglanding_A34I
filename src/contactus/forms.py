from django import forms



class ContactForm(forms.Form):
	full_name = forms.CharField()
	email = forms.EmailField()
	message = forms.CharField(widget=forms.Textarea)



	def clean_email(self):
		email = self.cleaned_data.get('email')
		email_base, provider = email.split("@")
		domain, extension = provider.split(".")
		return email

		# Great way to validate the form for domain specific emails or extenstions etc.. #
		# if not domain == "gmail":
		# 	raise forms.ValidationError("Please a valid gmail email address")
	# 	if not extension == "edu":
	# 		raise forms.ValidationError("Please a valid .edu email address")
	 	
	# def clean_full_name(self):
	# 	full_name = self.cleaned_data.get('full_name')
	# 	#could add validation code if needed here.. If not then this def is not needed and already runs in the background.
	# 	return full_name