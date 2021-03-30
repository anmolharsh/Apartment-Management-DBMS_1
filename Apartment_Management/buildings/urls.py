from django.contrib import admin
from django.urls import path,include
from . import views

app_name = 'buildings'

urlpatterns = [
	path('view/',views.view_main, name='main_view'),
   
	path('view/building/', views.view_building, name="building_details"),
	path('view/flat/',views.view_flat, name="flat_details"),
	path('view/service_directory/',views.view_service_directory, name="service_directory_details"),
	path('view/add_occupancy/',views.view_add_occupancy, name="add_occupancy"),
	path('view/view_occupancy/',views.view_occupancy, name="view_occupancy"),
	path('view/remove_occupancy/',views.remove_occupancy, name="remove_occupancy"),

]