from django import forms
from .models import Booking
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from bootstrap_datepicker_plus import DateTimePickerInput


class create_booking(forms.ModelForm):

    class Meta:
        model = Booking
        fields = ['facility','check_in','duration']
        widgets = {
        	'check_in' : DateTimePickerInput(),
        }