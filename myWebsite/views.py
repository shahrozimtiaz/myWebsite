from django.shortcuts import render, redirect, reverse
from django.core.mail import send_mail

def home(request):
    return render(request, 'myWebsite/home.html')

def projects(request):
    return render(request, 'myWebsite/projects.html')

def courseWork(request):
    return render(request, 'myWebsite/courseWork.html')

def contact(request):
    return render(request, 'myWebsite/contact.html')

def sent(request):
    return render(request, 'myWebsite/sent.html')

def fail(request):
    return render(request, 'myWebsite/sent.html')