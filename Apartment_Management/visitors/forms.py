from django import forms
from .models import Visitor
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from bootstrap_datepicker_plus import DateTimePickerInput
from searchableselect.widgets import SearchableSelect

class visitor_entry_form(forms.ModelForm):
	resident_name = forms.CharField(max_length = 20)
	
	def __init__(self, *args, **kwargs): 
	    super(forms.ModelForm, self).__init__(*args, **kwargs)
	    self.fields['fname'].label = 'First Name'
	    self.fields['lname'].label = 'Last Name'
	    self.fields['datetime_entry'].label = 'Entry Date & Time'


	class Meta :
		model = Visitor
		fields = ['fname','lname','phone','datetime_entry']
		widgets = {
			'resident_name' : SearchableSelect(model='User', search_field='first_name', limit=10),
			'datetime_entry' : DateTimePickerInput(),
		}
       

class visitor_exit_form(forms.ModelForm) :

	def __init__(self, *args, **kwargs): 
	    super(forms.ModelForm, self).__init__(*args, **kwargs)
	    self.fields['datetime_exit'].label = ''

	class Meta:
		model = Visitor
		fields = ['datetime_exit'] 
		widgets = {
			'datetime_exit' : DateTimePickerInput(),
		}