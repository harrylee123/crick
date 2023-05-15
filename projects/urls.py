from django.contrib import admin
from django.urls import path
from . import views # . means the same file path

#the below code links to the views.py where it takes the functions
urlpatterns = [
    path('', views.projects, name="projects"), # because there is an empty string at the start, nothing extra needs to be added to the url meaning that the basic url is the home page
    path('project/<str:pk>/', views.project, name="project") ## <str:PK> is a variable that can be used to add variation to a page
]