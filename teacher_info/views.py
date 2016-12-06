# -*- coding: utf-8 -*-
# coding=gbk
from __future__ import division
from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from rating.models import Teacher
# Create your views here.
from django.contrib.auth.decorators import login_required


def teacher_info(request):
	teachers =  Teacher.objects.all()
	# for t in teachers:
		# print "here is teacher %s, name %s" %(t.tid, t.name)

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

	# print "here is teacher %s, name %s" %(teacher.score1_content, teacher.name)
	# template = "teacher_info.html"
	# template = "teacher_widget.html"
	template = "profile.html"
	# template = "user_profile.html"


	
	score1_item = {'content':teacher.score1_content, 'score': teacher.score1, 'count':teacher.score1_count, 'score_percent': format(teacher.score1/10,'.0%')}
	score2_item = {'content':teacher.score2_content, 'score': teacher.score2, 'count':teacher.score2_count, 'score_percent': format(teacher.score2/10,'.0%')}
	score3_item = {'content':teacher.score3_content, 'score': teacher.score3, 'count':teacher.score3_count, 'score_percent': format(teacher.score3/10,'.0%')}
	score4_item = {'content':teacher.score4_content, 'score': teacher.score4, 'count':teacher.score4_count, 'score_percent': format(teacher.score4/10,'.0%')}
	score5_item = {'content':teacher.score5_content, 'score': teacher.score5, 'count':teacher.score5_count, 'score_percent': format(teacher.score5/10,'.0%')}
	score6_item = {'content':teacher.score6_content, 'score': teacher.score6, 'count':teacher.score6_count, 'score_percent': format(teacher.score6/10,'.0%')}
	score7_item = {'content':teacher.score7_content, 'score': teacher.score7, 'count':teacher.score7_count, 'score_percent': format(teacher.score7/10,'.0%')}
	score8_item = {'content':teacher.score8_content, 'score': teacher.score8, 'count':teacher.score8_count, 'score_percent': format(teacher.score8/10,'.0%')}
	score9_item = {'content':teacher.score9_content, 'score': teacher.score9, 'count':teacher.score9_count, 'score_percent': format(teacher.score9/10,'.0%')}
	score10_item = {'content':teacher.score10_content, 'score': teacher.score10, 'count':teacher.score10_content, 'score_percent': format(teacher.score10/10,'.0%')}

	score_item = [score1_item, score2_item, score3_item,score4_item,score5_item,score6_item,score7_item,score8_item,score9_item,score10_item]

	context = {
				"name": teacher.name,
				"major": teacher.major,
				# 'score1_item' : score1_item ,
				# 'score2_item' : score2_item ,
				# 'score3_item' : score3_item ,
				# 'score4_item' : score4_item ,
				# 'score5_item' : score5_item ,
				# 'score6_item' : score6_item ,
				# 'score7_item' : score7_item ,
				# 'score8_item' : score8_item ,
				# 'score9_item' : score9_item ,
				# 'score10_item': score10_item,
				'score_item': score_item,
				'count': teacher.score1_count,

				"intro": teacher.intro,

				}


	return render(request, template, context)
	# return HttpResponseRedirect("http://localhost:8000/")
