from django.shortcuts import render
from django.conf import settings 

# Create your views here.
def home(request):
	context = {}
	template = "index.html"

	return render(request,template, context)

