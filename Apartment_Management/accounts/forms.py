from django import forms
from .models import Resident,Watchmen
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class WatchmenSignup(forms.ModelForm):

    class Meta:
        model = Watchmen
        fields = ['phone','age','gender','address']

class ResidentSignup(forms.ModelForm):

    class Meta:
        model = Resident
        fields = ['phone','gender','age']

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username' ,'first_name' ,'last_name' ,'email' , 'password1','password2']

class user_update(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username','email']

class profile_pic_serv(forms.ModelForm):

    class Meta:
        model = Watchmen
        fields = ['image']

class profile_pic_res(forms.ModelForm):

    class Meta:
        model = Resident
        fields = ['image']

class edit_detail_serv(forms.ModelForm):

    class Meta:
        model = Watchmen
        fields = ['phone','age','gender','address']

class edit_detail_res(forms.ModelForm):

    class Meta:
        model = Resident
        fields = ['phone','gender','age']