from django.contrib import admin
from django.urls import path,include
from .import views
from django.http import HttpResponse
from django.shortcuts import render

app_name = 'accounts'


urlpatterns = [
    path('signup/', views.signup,name="signup"),
    path('login_user/', views.login_view , name='login_user'),
    path('logout_user/', views.logout_view , name='logout_user'),

    path('signup-watchmen/', views.signup_watchmen,name="signup_watchmen"),
    path('signup-Resident/',views.signup_resident,name="signup_resident"),
   
    path('edit-details/',views.edit_details,name="edit_details"),
    path('profile/',views.profile,name='profile'),
]