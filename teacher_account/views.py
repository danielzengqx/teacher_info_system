# -*- coding: utf-8 -*-
# coding=gbk

from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from rating.models import User
# Create your views here.

# Create your views here.
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