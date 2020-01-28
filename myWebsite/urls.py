from django.urls import path

from . import views

app_name = 'myWebsite'
urlpatterns = [
    path('', views.home, name='home'),
    path('projects/', views.projects, name='projects'),
    path('coursework/', views.courseWork, name='courseWork'),
    path('contact/', views.contact, name='contact'),
    path('sent/', views.sent, name='sent'),
]