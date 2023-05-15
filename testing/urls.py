
from django.contrib import admin
from django.urls import path, include #path function allows things to be displayed on page
# in charge of url system of entire app. control diff pages
# paths in the url 

urlpatterns = [ 
    path('admin/', admin.site.urls), # base url plus admin will go to admin.site.urls
    path('', include('projects.urls'))# will include all urls from projects.urls
]
