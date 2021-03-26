from django.urls import path

from . import views
app_name = 'complaints'


urlpatterns = [
    path('complaints/', views.complaints_display_view.as_view(), name='complaints_display'),
]