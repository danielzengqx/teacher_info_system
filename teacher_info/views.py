# -*- coding: utf-8 -*-
# coding=gbk
from __future__ import division
from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from rating.models import Teacher
# Create your views here.
from django.contrib.auth.decorators import login_required

def load_more(request, tab=1, page=0):
	teachers =  Teacher.objects.all()
	teachers_major1 = list()
	teachers_major2 = list()
	teachers_major3 = list()
	for t in teachers:
		if t.major == u"计算机":
			# print "here is teacher %s, name %s, major %s" %(t.tid, t.name, t.major)
			teachers_major1.append(t)
		elif t.major == u"音乐系":
			# print "here is teacher %s, name %s, major %s" %(t.tid, t.name, t.major)
			teachers_major2.append(t)
		else:
			teachers_major3.append(t)

	# template = "teacher_info.html"
	# template = "teacher_widget.html"
	# template = "profile.html"
	# template = "user_profile.html"
	template = "page_tab%s.html" %tab
	print template
	print teachers_major3
	page = int(page)
	context = {
				"teachers_major1": teachers_major1[:(page+1)*10],
				"teachers_major2": teachers_major2[:(page+1)*10],
				"teachers_major3": teachers_major3[:(page+1)*10]
				}


	return render(request, template, context)
	# return HttpResponseRedirect("http://localhost:8000/")


def teacher_init():
	teachers =  Teacher.objects.all()
	for t in teachers:
		# print "count %s type %s, star" %(t.score1_count, type(t.score1_count))
		if t.score1_count == 0:
			print "equals zero"
			t.stars_filled = ''
			t.stars_empty = 'xxxxx'
			t.save()
			# print "stars after %s" %t.stars_filled

def teacher_info(request, page=0):
	teacher_init()
	teachers =  Teacher.objects.all()
	teachers_major1 = list()
	teachers_major2 = list()
	teachers_major3 = list()
	for t in teachers:
		if t.major == u"计算机":
			# print "here is teacher %s, name %s, major %s" %(t.tid, t.name, t.major)
			teachers_major1.append(t)
		elif t.major == u"音乐系":
			# print "here is teacher %s, name %s, major %s" %(t.tid, t.name, t.major)
			teachers_major2.append(t)
		else:
			teachers_major3.append(t)

	# template = "teacher_info.html"
	# template = "teacher_widget.html"
	# template = "profile.html"
	# template = "user_profile.html"
	template = "tab.html"

	print teachers_major3
	page = int(page)
	context = {
				"teachers_major1": teachers_major1[page*10:(page+1)*10],
				"teachers_major2": teachers_major2[page*10:(page+1)*10],
				"teachers_major3": teachers_major3[page*10:(page+1)*10]


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


	
	score1_item = {'content':teacher.score1_content, 'score': int(round(teacher.score1)), 'count':teacher.score1_count, 'score_percent': format(teacher.score1/10,'.0%')}
	score2_item = {'content':teacher.score2_content, 'score': int(round(teacher.score2)), 'count':teacher.score2_count, 'score_percent': format(teacher.score2/10,'.0%')}
	score3_item = {'content':teacher.score3_content, 'score': int(round(teacher.score3)), 'count':teacher.score3_count, 'score_percent': format(teacher.score3/10,'.0%')}
	score4_item = {'content':teacher.score4_content, 'score': int(round(teacher.score4)), 'count':teacher.score4_count, 'score_percent': format(teacher.score4/10,'.0%')}
	score5_item = {'content':teacher.score5_content, 'score': int(round(teacher.score5)), 'count':teacher.score5_count, 'score_percent': format(teacher.score5/10,'.0%')}
	score6_item = {'content':teacher.score6_content, 'score': int(round(teacher.score6)), 'count':teacher.score6_count, 'score_percent': format(teacher.score6/10,'.0%')}
	score7_item = {'content':teacher.score7_content, 'score': int(round(teacher.score7)), 'count':teacher.score7_count, 'score_percent': format(teacher.score7/10,'.0%')}
	score8_item = {'content':teacher.score8_content, 'score': int(round(teacher.score8)), 'count':teacher.score8_count, 'score_percent': format(teacher.score8/10,'.0%')}
	score9_item = {'content':teacher.score9_content, 'score': int(round(teacher.score9)), 'count':teacher.score9_count, 'score_percent': format(teacher.score9/10,'.0%')}
	score10_item = {'content':teacher.score10_content, 'score': int(round(teacher.score10)), 'count':teacher.score10_content, 'score_percent': format(teacher.score10/10,'.0%')}

	score_item = [score1_item, score2_item, score3_item,score4_item,score5_item,score6_item,score7_item,score8_item,score9_item,score10_item]



	score_total_percent = format(teacher.score_total/100,'.0%')
	context = {	
				"name": teacher.name,
				"major": teacher.major,
				'score_item': score_item,
				'count': teacher.score1_count,

				"intro": teacher.intro,
				"score_total": int(round(teacher.score_total, 1)),
				"score_total_percent": score_total_percent

				}


	return render(request, template, context)
	# return HttpResponseRedirect("http://localhost:8000/")
