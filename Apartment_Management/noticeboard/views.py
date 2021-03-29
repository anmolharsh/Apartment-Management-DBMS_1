# Django imports
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, UpdateView, CreateView, DeleteView
from django.shortcuts import render,redirect
from django.http import HttpResponse
# Project imports
from .models import Notice
from .forms import NoticeForm


class NoticeListView(ListView):
    """ Allows you to list all notices. """
    model = Notice

def NoticeCreateView(request):
    if not request.user.is_authenticated:
        return redirect('/')

    if request.method == 'POST':
        form = NoticeForm(request.POST,request.FILES)
        if form.is_valid() :
            form.save()
            return redirect('success')

        return render(request,'noticeboard/notice_form.html',{'form': form,})


    else:
        form = NoticeForm()
        return render(request,'noticeboard/notice_form.html',{'form': form,})


def success(request):
    return redirect('noticeboard_notice_list')

class NoticeDetailView(DetailView):
    """ Allows you to view detailed information about an object in Notice. """
    model = Notice

class NoticeDeleteView(DeleteView):
    """ Allows you to delete a notice. """
    model = Notice
    success_url = reverse_lazy('noticeboard_notice_list')


class NoticeUpdateView(UpdateView):
    """ Allows you to update a notice's details. """
    model = Notice
    form_class = NoticeForm