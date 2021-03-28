from django.contrib import admin
from django.urls import path,include
from . import views

app_name = 'buildings'

urlpatterns = [
    # path('view/<int:user_id>/',views.view_main, name='main_view'),
   
    path('view/building/', views.view_building, name="building_details"),
    path('view/flat/',views.view_flat, name="flat_details"),
    path('view/service_directory/',views.view_service_directory, name="service_directory_details")
]