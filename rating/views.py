from django.shortcuts import render

# Create your views here.
from django.contrib.auth.decorators import login_required

@login_required(login_url='/register/')
def rating(request):
	user = request.user.username
	email = request.user.email

	template = "rating.html"
	context = {"username": user, 
				"email": email,
				}

	return render(request, template, context)


