from django.urls import path

from . import views

urlpatterns = [
    path('', views.complaints_display_view.as_view(), name='complaints_display'),
]