from django.urls import path

from . import views
app_name = 'visitors'

urlpatterns = [
	path('visitors-display/', views.visitors_display_view.as_view(), name='visitors_display'),
	path('visitors-watchman/', views.watchman_visitor_view.as_view(), name='visitors_watchman'),
	path('visitors-entry/', views.visitor_entry_view.as_view(), name='visitors_entry'),
	path('resident-error/', views.resident_error_view, name='resident_error'),
]

