# -*- coding: utf-8 -*-
# coding=gbk
from __future__ import division 
from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from models import Teacher
# Create your views here.
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_page
import json
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

		print "score 1 before %s" %teacher.score1

		teacher.score1 = teacher.score1 * teacher.score1_count

		print "score 1 before2 %s" %teacher.score1

		teacher.score2 = teacher.score2 * teacher.score2_count

		print "score 2 before %s" %teacher.score2
		teacher.score3 = teacher.score3 * teacher.score3_count
		teacher.score4 = teacher.score4 * teacher.score4_count
		teacher.score5 = teacher.score5 * teacher.score5_count
		teacher.score6 = teacher.score6 * teacher.score6_count
		teacher.score7 = teacher.score7 * teacher.score7_count
		teacher.score8 = teacher.score8 * teacher.score8_count
		teacher.score9 = teacher.score9 * teacher.score9_count
		teacher.score10 = teacher.score10 * teacher.score10_count

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

		print "score 1 count  %s" %teacher.score1_count
		# print "teacher %s name is %s" %(tid, teacher.name)
		teacher.score1 = (teacher.score1 + s1) / teacher.score1_count

		print "score 1 after %s" %teacher.score1

		teacher.score2 = (teacher.score2 + s2) / teacher.score2_count
		print "score 2 after %s" %teacher.score2

		teacher.score3 = (teacher.score3 + s3) / teacher.score3_count
		teacher.score4 = (teacher.score4 + s4) / teacher.score4_count
		teacher.score5 = (teacher.score5 + s5) / teacher.score5_count
		teacher.score6 = (teacher.score6 + s6) / teacher.score6_count
		teacher.score7 = (teacher.score7 + s7) / teacher.score7_count
		teacher.score8 = (teacher.score8 + s8) / teacher.score8_count
		teacher.score9 = (teacher.score9 + s9) / teacher.score9_count
		teacher.score10 = (teacher.score10 + s10) / teacher.score10_count
		teacher.score_total =   teacher.score1 + teacher.score2 + teacher.score3 + teacher.score4 + teacher.score5 + teacher.score6 + teacher.score7 + teacher.score8 + teacher.score9 + teacher.score10
		stars = int(round(teacher.score_total /100 * 5 ))
		teacher.stars_filled = stars * 'x'
		teacher.stars_empty = (5 - stars) * 'x'
		# print teacher.score_rater
		# print type(json.loads(teacher.score_rater))
		teacher.add_rater(user)

		print "here is stars %s, stars_filled %s, stars_empty %s" %(stars, teacher.stars_filled, teacher.stars_empty)


		print teacher.score_total
		teacher.save()
		return HttpResponseRedirect("/teacher_info/detail/%s" %tid)
		# return test_cache(request)


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


def redirect(request):
	template = "redirect.html"

	context = {
				}


	return render(request, template, context)

def success_redirect(request, tid):
	template = "success_redirect.html"

	context = {"tid" : tid,
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

@cache_page(5)
def test_cache(request):
	return HttpResponse("hello")


def check_rater(request, tid):
	user = request.user.username
	email = request.user.email
	teacher = Teacher.objects.get(tid=tid)
	print teacher.score_rater
	print "hererere"
	if user in json.loads(teacher.score_rater):
		print "in here"
		return HttpResponse("<p>您已对该教师进行过评分</p>")
	else:
		teachers =  Teacher.objects.all()
	# for t in teachers:
	# 	print "here is teacher %s, name %s" %(t.tid, t.name)
		template = "rating_form.html"

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

		context = {
					"score_contents": score_contents
					}


	return render(request, template, context)




