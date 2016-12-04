# -*- coding: utf-8 -*-
# coding=gbk
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
		s5 = int(request.POST['rating_4'])
		s6 = int(request.POST['rating_5'])
		s7 = int(request.POST['rating_6'])
		s8 = int(request.POST['rating_7'])
		s9 = int(request.POST['rating_8'])
		s10 = int(request.POST['rating_9'])

		print "Here is the scores ", s1, s2, s3, s4, type(tid)

		teacher = Teacher.objects.get(tid=tid)

 		teacher.score1_count = teacher.score1_count + 1
 		teacher.score2_count = teacher.score2_count + 1
 		teacher.score3_count = teacher.score3_count + 1
 		teacher.score4_count = teacher.score4_count + 1
 		teacher.score5_count = teacher.score5_count + 1
 		teacher.score6_count = teacher.score6_count + 1
 		teacher.score7_count = teacher.score7_count + 1
 		teacher.score8_count = teacher.score8_count + 1
 		teacher.score9_count = teacher.score9_count + 1
 		teacher.score10_count = teacher.score10_count + 1

		# print "teacher %s name is %s" %(tid, teacher.name)
		teacher.score1 = (teacher.score1 + s1) / teacher.score1_count
		teacher.score2 = (teacher.score2 + s2) / teacher.score2_count
		teacher.score3 = (teacher.score3 + s3) / teacher.score3_count
		teacher.score4 = (teacher.score4 + s4) / teacher.score4_count
		teacher.score5 = (teacher.score5 + s5) / teacher.score5_count
		teacher.score6 = (teacher.score6 + s6) / teacher.score6_count
		teacher.score7 = (teacher.score7 + s7) / teacher.score7_count
		teacher.score8 = (teacher.score8 + s8) / teacher.score8_count
		teacher.score9 = (teacher.score9 + s9) / teacher.score9_count
		teacher.score10 = (teacher.score10 + s10) / teacher.score10_count

		teacher.save()


	teachers =  Teacher.objects.all()
	# for t in teachers:
	# 	print "here is teacher %s, name %s" %(t.tid, t.name)

	score_contents = list()
	score_contents.append(teachers[0].score1_content)
	score_contents.append(teachers[0].score2_content)
	score_contents.append(teachers[0].score3_content)
	score_contents.append(teachers[0].score4_content)
	score_contents.append(teachers[0].score5_content)
	score_contents.append(teachers[0].score6_content)
	score_contents.append(teachers[0].score7_content)
	score_contents.append(teachers[0].score8_content)
	score_contents.append(teachers[0].score9_content)
	score_contents.append(teachers[0].score10_content)		

	# for i in score_contents:
	# 	print i
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


