from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from rating.models import Teacher
# Create your views here.
from django.contrib.auth.decorators import login_required

def teacher_info(request):
	# user = request.user.username
	# email = request.user.email
	# user = "test"
	# email = "test@test.com"


	teachers =  Teacher.objects.all()
	for t in teachers:
		print "here is teacher %s, name %s" %(t.tid, t.name)

	template = "teacher_info.html"
	context = {
				"teachers": teachers
				}


	return render(request, template, context)
	# return HttpResponseRedirect("http://localhost:8000/")


import uuid 
def get_ref_id():
	ref_id = str(uuid.uuid4())[:11].replace('-', '').lower()
	try:
		id_exists = User.objects.get(ref_id=ref_id)
		return id_exists
	except:
		return ref_id


