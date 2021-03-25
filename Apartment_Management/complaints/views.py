from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import generic

from .models import Complaints

# Create your views here.
class complaints_display_view(generic.ListView) :
	model = Complaints
	template_name = 'complaints/complaints_display.html'
	context_object_name = 'complaints_list'
	
	def get_queryset(self) :
		print(Complaints.objects.all().values())
		return Complaints.objects.all()

	def get_context_data(self, **kwargs):
	    context = super().get_context_data(**kwargs)
	    field_names  = [f.name for f in Complaints._meta.get_fields()]
	    context['column_headers'] = field_names
	    return context


