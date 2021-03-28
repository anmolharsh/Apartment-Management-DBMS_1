from django.urls import path

from . import views
app_name = 'complaints'


urlpatterns = [
    path('complaints-list/', views.complaints_display_view.as_view(), name='complaints_display'),
    path('complaints-lodge/', views.lodge_complaint_view.as_view(), name='lodge_complaint'),
    path('complaints-admin/', views.admin_complaint_view.as_view(), name='admin-complaint'),
]