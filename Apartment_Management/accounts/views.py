from django.http import HttpResponse
from django.shortcuts import render

def signup(request):
	return HttpResponse('signup')

def login_view(request):
	return HttpResponse('login_view')

def logout_view(request):
	return HttpResponse('logout_view')

def signup_employee(request):
	return HttpResponse('signup_employee')

def signup_customer(request):
	return HttpResponse('signup_customer')

def profile(request):
	return HttpResponse('profile')

def edit_details(request):
	return HttpResponse('edit_details')
