from django.shortcuts import render
from .models import Comment
# Create your views here.
def comment(request):
	template = "comment_simple.html"

	if request.POST:
		content = request.POST["comment"]
		author = request.user.username
		comment =  Comment(content=content, author=author)

		comment.save()




	comments = Comment.objects.all().order_by('time')


	context = {
				"comments": comments[::-1],

				}


	return render(request, template, context)
