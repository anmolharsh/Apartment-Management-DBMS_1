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
		user_id = self.request.user.id
		return Complaints.objects.filter(user_id__exact = user_id)

	def get_context_data(self, **kwargs):
	    context = super().get_context_data(**kwargs)
	    context['user_id'] = self.request.user.id
	    resident = Resident.objects.get(user_id__exact = self.request.user.id)
	    context['image_url'] = resident.image.url
	    return context


class lodge_complaint_view(FormView) :
	model = Complaints
	form_class = lodge_complaint
	template_name = 'complaints/complaint_register.html'
	
	def dispatch(self, request, *args, **kwargs) :
		self.success_url = reverse_lazy('complaints:complaints_display')
		return super().dispatch(request,args,kwargs)

	def get_context_data(self, **kwargs):
	    context = super().get_context_data(**kwargs)
	    context['complaint_form'] = self.form_class
	    return context

	def form_valid(self, form) :
		complaint = form.save(commit = False)
		complaint.user_id = Resident.objects.get(user__exact = self.request.user)
		complaint.save()
		return super().form_valid(form)

class admin_complaint_view(generic.ListView) :
	model = Complaints
	template_name = 'complaints/complaints_admin.html'

	def get_context_data(self, **kwargs):
	    context = super().get_context_data(**kwargs)
	    context['user_id'] = self.request.user.id
	    image_url_list = []
	    full_name_list = []
	    complaints_list = self.model.objects.all() 
	    for c in complaints_list :
	    	resident = Resident.objects.get(user__exact = c.user_id)
	    	full_name = resident.user.first_name + " " + resident.user.last_name
	    	full_name_list.append(full_name)
	    	image_url_list.append(resident.image.url)
	    context['values'] = zip(full_name_list, image_url_list, complaints_list)
	    return context

	def post(self, request, **kwargs) :
		if request.POST['complaint_id'] :
			complaint_id = request.POST['complaint_id']
			complaint = Complaints.objects.get(complaint_id__exact = complaint_id)

		if request.POST['comments']:
			comments = request.POST['comments']
			complaint.comments = comments
		
		if request.POST['status'] != "" :
			status = request.POST['status']
			complaint.status = status	
		
		complaint.save()
		
		return HttpResponseRedirect(reverse_lazy('complaints:admin-complaint'))



