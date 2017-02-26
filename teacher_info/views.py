# -*- coding: utf-8 -*-
# coding=gbk
from __future__ import division
from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from rating.models import Teacher2, RatingForTeacher
# Create your views here.
from django.contrib.auth.decorators import login_required
import inspect

def lineno():
    """Returns the current line number in our program."""
    return inspect.currentframe().f_back.f_lineno

def load_more(request, tab=1, page=0):
	teachers =  Teacher2.objects.all()
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
	teachers =  Teacher2.objects.all()
	for t in teachers:
		# print "count %s type %s, star" %(t.score1_count, type(t.score1_count))
		if t.score_total == 0:
			print "equals zero"
			t.stars_filled = ''
			t.stars_empty = 'xxxxx'
			t.save()
			# print "stars after %s" %t.stars_filled

def teacher_info(request, page=0):
	teacher_init()
	teachers =  Teacher2.objects.all()
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

def teacher_detail(request, id):
	try:
		teacher =  Teacher2.objects.get(id=id)
	except Exception as e:
		print lineno(), "Failed Reason, ", e
		HttpResponse("不存在该资源")

	template = "profile.html"


	score_total_percent = format(teacher.score_total/100,'.0%')
	context = {	
				"name": teacher.name,
				"major": teacher.major,
				'count': teacher.rater_count,
				"intro": teacher.intro,
				"score_total": int(round(teacher.score_total, 1)),
				"score_total_percent": score_total_percent

				}


	return render(request, template, context)
