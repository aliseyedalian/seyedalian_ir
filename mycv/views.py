from django.shortcuts import render
from django.http import FileResponse
import os

# Create your views here.
def home(request):
	return render(request,'index.html',{})

def about(request):
	return render(request,'about.html',{})

def blogs(request):
	return render(request,'blogs.html',{})

def resume(request):
	filepath = os.path.join('static', 'resume/resume.pdf')
	return FileResponse(open(filepath, 'rb'), content_type='application/pdf')