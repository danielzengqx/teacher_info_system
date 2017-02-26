# -*- coding: utf-8 -*-
# coding=gbk

from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from rating.models import User, Profile, Teacher2
# Create your views here.
import inspect

def lineno():
    """Returns the current line number in our program."""
    return inspect.currentframe().f_back.f_lineno
def register(request):
	context = {}
	template = "teacher_signup.html"

	return render(request,template, context)



def signup(request):
	print request.POST
	user = User.objects.create_user(request.POST['full_name'].strip(), request.POST['email'].strip(), request.POST['password'].strip())
	user.profile.work_id = request.POST['work_id']
	user.profile.gender = request.POST['gender']
	user.first_name = user.username[1:]
	user.last_name = user.username[0]
	# user.is_active = False
	user.save()	
	# auth_mail(user)



	return HttpResponseRedirect('/')


def success(request):
	# questions_preview = [1,2,3,4,5]
	context = {}
	template = "register.html"

	return HttpResponse("Success")	


def setting(request):
	template = "setting.html"


	# wid = request.user.wid
	profile = Profile.objects.get(user=request.user)


	work_id = profile.work_id
	# return HttpResponseRedirect('/')
	if work_id:
		return HttpResponseRedirect("my_page/%s" %work_id)	
	else:
		return HttpResponse("Not a Teacher, please go back")	


def my_page(request, work_id):
	template = "my_page.html"
	# work_id = '20170002'

	profile = Profile.objects.get(work_id=work_id)
	try:
		teacher =  Teacher2.objects.get(work_id=work_id)

	except Exception as e:
		print lineno(), "Failed Reason, ", e
		HttpResponse("不存在该资源")



	score_total_percent = format(teacher.score_total/100,'.0%')
	context = {	
				"name": teacher.name,
				"major": teacher.major,
				'count': teacher.rater_count,
				"intro": teacher.intro,
				"score_total": int(round(teacher.score_total, 1)),
				"score_total_percent": score_total_percent,
				"courses": teacher.all_courses.all()

				}


	return render(request,template, context)


def edit_page(request, work_id):
	template = "my_page.html"
	# work_id = '20170002'

	profile = Profile.objects.get(work_id=work_id)
	try:
		teacher =  Teacher2.objects.get(work_id=work_id)

	except Exception as e:
		print lineno(), "Failed Reason, ", e
		HttpResponse("不存在该资源")



	score_total_percent = format(teacher.score_total/100,'.0%')
	context = {	
				"name": teacher.name,
				"major": teacher.major,
				'count': teacher.rater_count,
				"intro": teacher.intro,
				"score_total": int(round(teacher.score_total, 1)),
				"score_total_percent": score_total_percent

				}


	return render(request,template, context)
