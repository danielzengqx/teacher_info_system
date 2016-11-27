from django.shortcuts import render

# Create your views here.
def comment(request):
	template = "comment_simple.html"

	context = {
				# "username": user, 
				# "email": email,
				# "teachers": teachers,
				# "score_contents": score_contents
				}


	return render(request, template, context)
