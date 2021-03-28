from django.urls import path

from . import views
app_name = 'bookings'


urlpatterns = [
    path('bookings-list/', views.bookings_display_view.as_view(), name='bookings_display'),  
    path('bookings-create/', views.create_booking_view.as_view(), name='create_booking'),
    path('bookings-admin/', views.admin_bookings_view.as_view(), name='admin-booking'),
]

