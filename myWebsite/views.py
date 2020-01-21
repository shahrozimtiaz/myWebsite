from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

def home(request):
    return render(request, 'myWebsite/home.html')

def projects(request):
    return render(request, 'myWebsite/projects.html')

def courseWork(request):
    return render(request, 'myWebsite/courseWork.html')

def contact(request):
    return render(request, 'myWebsite/contact.html')
