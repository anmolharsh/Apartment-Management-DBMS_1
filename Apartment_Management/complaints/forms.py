from django import forms
from .models import Complaints
from django.db import models
from phone_field import PhoneField
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class lodge_complaint(forms.ModelForm):

    class Meta:
        model = Complaints
        fields = ['content']