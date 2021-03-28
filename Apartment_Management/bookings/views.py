from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django import forms
from django.views.generic.edit import FormView

from .models import Booking
from accounts.models import Resident
from .forms import create_booking

# Create your views here.
class bookings_display_view(generic.ListView) :
	model = Booking
	template_name = 'bookings/bookings_display.html'
	context_object_name = 'bookings_list'

	def get_queryset(self) :
		user_id = self.request.user.id
		return Booking.objects.filter(user_id__exact = user_id)

	def get_context_data(self, **kwargs):
	    context = super().get_context_data(**kwargs)
	    context['user_id'] = self.request.user.id
	    resident = Resident.objects.get(user_id__exact = self.request.user.id)
	    context['image_url'] = resident.image.url
	    return context

class create_booking_view(FormView) :
	model = Booking
	form_class = create_booking
	template_name = 'bookings/booking_create.html'
	
	def dispatch(self, request, *args, **kwargs) :
		self.success_url = reverse_lazy('bookings:bookings_display')
		return super().dispatch(request,args,kwargs)

	def get_context_data(self, **kwargs):
	    context = super().get_context_data(**kwargs)
	    context['booking_form'] = self.form_class
	    return context

	def form_valid(self, form) :
		booking = form.save(commit = False)
		booking.user_id = Resident.objects.get(user__exact = self.request.user)
		booking.save()
		return super().form_valid(form)