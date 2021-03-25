from django import forms
from .models import Resident,Watchmen
from django.db import models
from phone_field import PhoneField
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class WatchmenSignup(forms.ModelForm):

    class Meta:
        model = Watchmen
        fields = ['name','phone','age','gender','address']

class ResidentSignup(forms.ModelForm):

    class Meta:
        model = Resident
        fields = ['name','age']

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username' ,'email' , 'password1','password2']

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
        fields = ['name','phone','age','gender','address']

class edit_detail_res(forms.ModelForm):

    class Meta:
        model = Resident
        fields = ['name','age']