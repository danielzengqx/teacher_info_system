from django.shortcuts import render, HttpResponse, HttpResponseRedirect


# Create your views here.
def video(request):
	# user = request.user.username
	# email = request.user.email
	# user = "test"
	# email = "test@test.com"


	template = "video.html"
	context = {
				}


	return render(request, template, context)
	# return HttpResponseRedirect("http://localhost:8000/")



