# -*- coding: utf-8 -*-
# coding=gbk

from django.shortcuts import render, HttpResponse
from django.conf import settings 
from models import User
from django.contrib.auth.models import User

# Create your views here.
def register(request):

	# registerInfo = {'username':'用户名', 'password':'密码','pwdconfirm':'确认密码', 'email':'邮箱'}
	context = {}
	template = "register.html"

	return render(request,template, context)


import uuid 
def get_ref_id():
	ref_id = str(uuid.uuid4())[:11].replace('-', '').lower()
	try:
		id_exists = User.objects.get(ref_id=ref_id)
		return id_exists
	except:
		return ref_id

#daniel made
# def signup(request):
# 	# context = {'username':user_name}
# 	template = "register.html"
# 	print "here is post" , request.POST

# 	user = User()
# 	user.name = request.POST['user_name']
# 	user.passwd = request.POST['password']
# 	user.email = request.POST['email']
# 	user.u_id = request.POST['uid']
# 	user.save()

def signup(request):
	print request.POST
	user = User.objects.create_user(request.POST['user_name'], request.POST['email'], request.POST['password'])
	user.save()

	return HttpResponse(request.POST['user_name'])

def success(request):
	# questions_preview = [1,2,3,4,5]
	context = {}
	template = "register.html"

	return HttpResponse("Success")
