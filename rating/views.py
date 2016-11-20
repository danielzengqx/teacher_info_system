from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from models import Teacher
# Create your views here.
from django.contrib.auth.decorators import login_required

@login_required(login_url='/rating/redirect/')
def rating(request):
	user = request.user.username
	email = request.user.email
	# user = "test"
	# email = "test@test.com"

	if 	request.POST:
		print "here is rating post %s" %request.POST

		tid = request.POST['m1']
		s1 = int(request.POST['rating_0'])
		s2 = int(request.POST['rating_1'])
		s3 = int(request.POST['rating_2'])
		s4 = int(request.POST['rating_3'])

		print "Here is the scores ", s1, s2, s3, s4, type(tid)



		teacher = Teacher.objects.get(tid=tid)
		print "teacher %s name is %s" %(tid, teacher.name)
		teacher.score1 = s1
		teacher.score2 = s2
		teacher.score3 = s3
		teacher.score4 = s4
		teacher.save()


	teachers =  Teacher.objects.all()
	# for teachers:
	# print "here is teacher %s, name %s" %(t.tid, t.name)
	score_contents = list()
	score_contents.append(teachers[0].score1_content)
	score_contents.append(teachers[0].score2_content)
	score_contents.append(teachers[0].score3_content)
	score_contents.append(teachers[0].score4_content)

	for i in score_contents:
		print i
	template = "rating.html"

	context = {"username": user, 
				"email": email,
				"teachers": teachers,
				"score_contents": score_contents
				}


	return render(request, template, context)
	# return HttpResponseRedirect("http://localhost:8000/")


def redirect(request):
	template = "redirect.html"

	context = {
				}


	return render(request, template, context)

import uuid 
def get_ref_id():
	ref_id = str(uuid.uuid4())[:11].replace('-', '').lower()
	try:
		id_exists = User.objects.get(ref_id=ref_id)
		return id_exists
	except:
		return ref_id


