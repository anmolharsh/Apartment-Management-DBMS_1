from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django import forms
from django.views.generic.edit import FormView
from .models import Visitor
from .forms import visitor_exit_form, visitor_entry_form
from accounts.models import Resident
from django.contrib.auth.models import User

# Create your views here.
class visitors_display_view(generic.ListView) :
	model = Visitor
	template_name = 'visitors/visitors_display.html'
	context_object_name = 'visitors_list'

	def get_queryset(self) :
		user_id = self.request.user.id
		return Visitor.objects.filter(user_id__exact = user_id)

	def get_context_data(self, **kwargs):
	    context = super().get_context_data(**kwargs)
	    return context

	def post(self, request, **kwargs) :
		if request.POST['status'] and request.POST['visitor_id']:
			status = request.POST['status']
			visitor_id = request.POST['visitor_id']
			visitor = Visitor.objects.get(visitor_id__exact = visitor_id)
			visitor.status = status
			visitor.save()
		
		return HttpResponseRedirect(reverse_lazy('visitors:visitors_display'))

class watchman_visitor_view(FormView) :
	model = Visitor
	form_class = visitor_exit_form
	template_name = 'visitors/visitors_watchman.html'

	def dispatch(self, request, *args, **kwargs) :
		self.success_url = reverse_lazy('visitors:visitors_watchman')
		return super().dispatch(request,args,kwargs)

	def get_context_data(self, **kwargs):
	    context = super().get_context_data(**kwargs)
	    full_name_list = []
	    visitors_list = self.model.objects.all() 
	    for c in visitors_list :
	    	resident = Resident.objects.get(user__exact = c.user_id)
	    	full_name = resident.user.first_name + " " + resident.user.last_name
	    	full_name_list.append(full_name)
	    context['values'] = zip(full_name_list, visitors_list)
	    return context

	def form_valid(self, form) :
		visitor = form.save(commit = False)
		v = Visitor.objects.get(visitor_id__exact = self.request.POST['visitor_id'])
		v.datetime_exit = visitor.datetime_exit
		v.save()
		return super().form_valid(form)

class visitor_entry_view(FormView) :
	model = Visitor
	form_class = visitor_entry_form
	template_name = 'visitors/visitors_entry.html'

	def dispatch(self, request, *args, **kwargs) :
		self.success_url = reverse_lazy('visitors:visitors_watchman')
		return super().dispatch(request,args,kwargs)

	def get_context_data(self, **kwargs):
	    context = super().get_context_data(**kwargs)
	    return context

	def form_valid(self, form) :
		visitor = form.save(commit = False)
		try :
			r = Resident.objects.get(user_id__first_name__iexact = form.cleaned_data['resident_name'])
			visitor.user_id = r
			visitor.save()
		except :
			self.success_url = reverse_lazy('visitors:resident_error')
		return super().form_valid(form)

def resident_error_view(request) :
	return render(request,'visitors/resident_entry_error.html')
