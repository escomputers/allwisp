from django.shortcuts import render
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from . import views


urlpatterns =[
	
	# # # DEFAULT
		path ('', views.index, name='index'),
		path ('login/', views.login_view, name='login'),
    	path ('logout/',views.logout_view, name='logout'),
   	 	path ('users/', views.users, name='users'),
    	path ('settings/', views.settings, name='settings'),
]
