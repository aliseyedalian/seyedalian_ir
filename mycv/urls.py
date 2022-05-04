from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('blogs.html',views.blogs,name='blogs'),
    path('resume.pdf',views.resume,name='resume'),
]
