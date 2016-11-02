from django.shortcuts import render, HttpResponse, HttpResponseRedirect

# Create your views here.
from django.contrib.auth.decorators import login_required

@login_required(login_url='/register/')
def rating(request):
	print "here is rating post %s" %request.POST
	user = request.user.username
	email = request.user.email
	# user = "test"
	# email = "test@test.com"
	template = "index.html"
	context = {"username": user, 
				"email": email,
				}


	# return render(request, template, context)
	return HttpResponseRedirect("http://localhost:8000/")


import uuid 
def get_ref_id():
	ref_id = str(uuid.uuid4())[:11].replace('-', '').lower()
	try:
		id_exists = User.objects.get(ref_id=ref_id)
		return id_exists
	except:
		return ref_id

def signup(request):
	# context = {'username':user_name}
	template = "register.html"
	print "here is post" , request.POST

	user = User()
	user.name = request.POST['user_name']
	user.passwd = request.POST['password']
	user.email = request.POST['email']
	user.u_id = request.POST['uid']
	user.save()
