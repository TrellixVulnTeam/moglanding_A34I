from django.shortcuts import render

from .forms import SignUpForm

# Create your views here.
def home(request):
	title = 'Welcome'
	form = SignUpForm(request.POST or None)
	# Example
	# if request.user.is_authenticated():
	# 	title = "Logged in user : %s" %(request.user)

	# if you want to see what the request.POST is doing
	# if request.method == "POST":
	# 	print(request.POST)
	context = {
		"title": title,
		"form": form

	}
	

	if form.is_valid():
		
		#form instance - capturing this form at this instance
		instance = form.save(commit=False)
		
		# if they dont fill out their name lets set it as a GuestUser
		if not instance.full_name:
			instance.full_name = "GuestUser"

		# in order to actually save
		instance.save()
		# print the instance
		print(instance)
		context = {
			"title": "Yay Submission"
		}

	return render(request, "home.html", context)