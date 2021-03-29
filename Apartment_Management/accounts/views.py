from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .forms import WatchmenSignup,ResidentSignup,UserRegisterForm,user_update,profile_pic_serv,profile_pic_res,edit_detail_res,edit_detail_serv
from django.contrib.auth import login,logout
from .models import Resident,Watchmen,Profile
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from PIL import Image
from django.core.files.base import ContentFile
from django.urls import reverse_lazy

#resident:p
def signup_resident(request):

    if request.user.is_authenticated and not request.user.is_superuser:
        return redirect('home')

    if request.method == 'POST':
        user_form = UserRegisterForm(request.POST)
        details_form = ResidentSignup(request.POST)

        if user_form.is_valid() and details_form.is_valid():
            cur_user = user_form.save()
            prof1 = Profile()
            prof1.user = cur_user
            prof1.type = "P"
            prof1.save()
            res = details_form.save(commit=False)
            res.user = cur_user
            res.save()
            #login(request,cur_user)
            return redirect('/')
        else:
            context = {
                'user_form': user_form,
                'details_form': details_form
            }
            return render(request,'accounts/signup.html',context)

    user_form = UserRegisterForm()
    details_form = ResidentSignup()
    context = {
        'user_form': user_form,
        'details_form': details_form,
        'flag': 1
    }
    return render(request,'accounts/signup.html',context)

def signup_watchmen(request):
    if  request.user.is_authenticated and not request.user.is_superuser :
        return redirect('home')

    if request.method == 'POST':
        user_form = UserRegisterForm(request.POST)
        details_form = WatchmenSignup(request.POST,request.FILES)


        if user_form.is_valid() and details_form.is_valid():
            cur_user = user_form.save()
            serv = details_form.save(commit=False)
            serv.user = cur_user
            serv.save()
            prof1 = Profile()
            prof1.user = cur_user
            prof1.type = "D"
            prof1.save()
            serv = details_form.save(commit=False)
            serv.user = cur_user
            serv.save()

            #login(request,cur_user)
            return redirect('/')
        else:
            context = {
                'user_form': user_form,
                'details_form': details_form,
                'flag':0
            }
            return render(request,'accounts/signup.html',context)

    user_form = UserRegisterForm()
    details_form = WatchmenSignup()
    context = {
        'user_form': user_form,
        'details_form': details_form
    }
    return render(request,'accounts/signup.html',context)

def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('/')
    else:
        form = AuthenticationForm()
    return render(request,'accounts/login.html',{'form':form})

@login_required(login_url="/login_user/")
def profile(request):
    if request.method == 'POST':
        if request.user.profile.type == 'D':
            user_form = user_update(request.POST, instance=request.user)
            pic_form = profile_pic_serv(request.POST,request.FILES,instance=request.user.watchmen)
            edit_form = edit_detail_serv(request.POST,instance = request.user.watchmen)


            if user_form.is_valid() and pic_form.is_valid() and edit_form.is_valid():
                user_form.save()
                pic_form.save()
                edit_form.save()
                messages.success(request, f'Your Account Has been Updated')
                return redirect('home')

            context = {
                'user_form': user_form,
                'pic_form': pic_form,
                'edit_form': edit_form
            }
            return render(request, 'accounts/profile.html', context)

        else:
            user_form = user_update(request.POST, instance=request.user)
            pic_form = profile_pic_res(request.POST,request.FILES,instance=request.user.resident)
            edit_form = edit_detail_res(request.POST,instance=request.user.resident)

            if user_form.is_valid() and pic_form.is_valid() and edit_form.is_valid():
                user_form.save()
                pic_form.save()
                edit_form.save()
                messages.success(request, f'Your Account Has been Updated')
                return redirect('home')

            context = {
                'user_form': user_form,
                'pic_form': pic_form,
                'edit_form': edit_form
            }
            return render(request, 'accounts/profile.html', context)

    else:
        if request.user.profile.type == 'D':
            user_form = user_update(instance = request.user)
            pic_form = profile_pic_serv(instance = request.user.watchmen)
            edit_form = edit_detail_serv(instance = request.user.watchmen)

            context = {
                'user_form': user_form,
                'pic_form': pic_form,
                'edit_form': edit_form
            }
            return render(request, 'accounts/profile.html', context)

        else:
            user_form = user_update(instance = request.user)
            pic_form = profile_pic_res(instance = request.user.resident)
            edit_form = edit_detail_res(instance=request.user.resident)
            context = {
                'user_form': user_form,
                'pic_form': pic_form,
                'edit_form': edit_form
            }
            return render(request, 'accounts/profile.html', context)
@login_required(login_url="/login_user/")
def edit_details(request):
    if request.method == 'POST':
        if request.user.profile.type == 'D':
            form = edit_detail_serv(request.POST,instance=request.user.watchmen)

            if form.is_valid():
                form.save()
                messages.success(request, f'Details Updated')
                return redirect('accounts:profile')

            return render(request,'accounts/edit_details.html',{'form':form})

        else:
            form = edit_detail_res(request.POST,instance=request.user.resident)

            if form.is_valid():
                form.save()
                messages.success(request, f'Details Updated')
                return redirect('accounts:profile')

            return render(request,'accounts/edit_details.html',{'form':form})

    else:
        if request.user.profile.type == 'D':
            form = edit_detail_serv(instance = request.user.watchmen)
            return render(request,'accounts/edit_details.html',{'form':form})
        else:
            form = edit_detail_res(instance= request.user.resident)
            return render(request,'accounts/edit_details.html',{'form':form})


def signup(request):
    if request.user.is_authenticated and not request.user.is_superuser:
        return redirect('home')

    return render(request,'accounts/signup.html')

@login_required(login_url="/login_user/")
def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('home')
    else:
        return redirect('home')

