# -*- coding: utf-8 -*-
# coding=gbk

from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.conf import settings 
# from models import User
from django.contrib.auth.models import User
from django.core.mail import send_mail
import sys

reload(sys)
sys.setdefaultencoding('utf-8')
def auth_mail(user):
	print "sending email"
	send_mail(
    'Subject here',
    'Here is the user, 学号 %s 班级 %s 姓名 %s.' %(user.profile.school_num, user.profile.class_num, user.username),
    'cheer_zeng@163.com',
    ['love_mainana@163.com'],
    fail_silently=False,
)

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



def signup(request):
	print request.POST
	user = User.objects.create_user(request.POST['fullname'].strip(), request.POST['email'].strip(), request.POST['password'].strip())
	user.profile.school_num = request.POST['school_num']
	user.profile.class_num = request.POST['class_num']
	user.first_name = user.username[1:]
	user.last_name = user.username[0]
	user.is_active = False
	user.save()	
	auth_mail(user)



	return HttpResponseRedirect('/')

def success(request):
	# questions_preview = [1,2,3,4,5]
	context = {}
	template = "register.html"

	return HttpResponse("Success")
