from django.urls import path

from . import views
app_name = 'complaints'


urlpatterns = [
    path('<int:user_id>/complaints-list/', views.complaints_display_view.as_view(), name='complaints_display'),
    path('<int:user_id>/complaints-lodge/', views.lodge_complaint_view.as_view(), name='lodge_complaint'),
]