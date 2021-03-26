from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django import forms
from django.views.generic.edit import FormView

from accounts.models import Resident
from .models import Complaints
from .forms import lodge_complaint

# Create your views here.
class complaints_display_view(generic.ListView) :
	model = Complaints
	template_name = 'complaints/complaints_display.html'
	context_object_name = 'complaints_list'

	def get_queryset(self) :
		user_id = self.kwargs['user_id']
		return Complaints.objects.filter(user_id__exact = user_id)

	def get_context_data(self, **kwargs):
	    context = super().get_context_data(**kwargs)
	    field_names  = [f.name for f in Complaints._meta.get_fields()]
	    context['column_headers'] = field_names
	    context['user_id'] = self.kwargs['user_id']
	    return context


class lodge_complaint_view(FormView) :
	model = Complaints
	form_class = lodge_complaint
	template_name = 'complaints/complaint_register.html'
	
	def dispatch(self, request, *args, **kwargs) :
		self.success_url = reverse_lazy('complaints:complaints_display',kwargs = {'user_id' : kwargs['user_id']})
		self.user = Resident.objects.get(id__exact = kwargs['user_id'])
		return super().dispatch(request,args,kwargs)

	def get_context_data(self, **kwargs):
	    context = super().get_context_data(**kwargs)
	    context['complaint_form'] = self.form_class
	    return context

	def form_valid(self, form) :
		complaint = form.save(commit = False)
		complaint.user_id = self.user
		complaint.save()
		return super().form_valid(form)



