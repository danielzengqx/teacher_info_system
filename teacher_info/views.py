# -*- coding: utf-8 -*-
# coding=gbk
from __future__ import division
from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from rating.models import Teacher
# Create your views here.
from django.contrib.auth.decorators import login_required


def teacher_info(request):
	teachers =  Teacher.objects.all()
	for t in teachers:
		print "here is teacher %s, name %s" %(t.tid, t.name)

	# template = "teacher_info.html"
	# template = "teacher_widget.html"
	# template = "profile.html"
	template = "user_profile.html"



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

def teacher_detail(request, tid):
	try:
		teacher =  Teacher.objects.get(tid=tid)
	except:
		HttpResponse("不存在该资源")

	print "here is teacher %s, name %s" %(teacher.score1_content, teacher.name)
	# template = "teacher_info.html"
	# template = "teacher_widget.html"
	template = "profile.html"
	# template = "user_profile.html"



	context = {
				"name": teacher.name,
				"major": teacher.major,
				"score1": format(teacher.score1/10,'.2%'),
				"score1_content": teacher.score1_content,
				"score2":  format(teacher.score2/10,'.2%'),
				"score2_content": teacher.score2_content,
				"score3":  format(teacher.score3/10,'.2%'),
				"score3_content": teacher.score3_content,
				"intro": teacher.intro,

				}


	return render(request, template, context)
	# return HttpResponseRedirect("http://localhost:8000/")
