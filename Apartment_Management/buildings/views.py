from django.shortcuts import render,redirect
from .models import Building, Flat, Service_Directory, Occupies

# Create your views here.


# def view_main(request):
	# model = Occupies.filter(user = request.user)
	# render


def view_flat(request):
	# model = Occupies.objects.filter(user_id = 1)
	# flat_model = []
	# for i in model:
	# 	flat_model += Flat.objects.filter(flat_id = i.flat_id)
	# # render
	cnt = 0
	new_dict = []
	# for i in flat_model:
	# 	new_dict = {cnt:i}
	# 	cnt+=1
	print(cnt)
	return render(request, 'buildings/flat.html', {'new_dict':new_dict})


def view_building(request):
	# model = Occupies.objects.filter(user_id = request.user)
	# for i in model:
	# 	flat_model += Flat.objects.filter(flat_id = i.flat_id)
	# building_model = Building.objects.filter(building_id = flat_model.building_id)
	# # render
	# return render(request, 'buildings/building.html', building_model)
	cnt = 0
	print(cnt)

def view_service_directory(request):
	# model = Occupies.objects.filter(user_id = request.user)
	# flat_model = []
	# for i in model:
	# 	flat_model += Flat.objects.filter(flat_id = i.flat_id)
	# service_directory_model = []
	# for i in flat_model:
	# 	service_directory_model += Service_Directory.objects.filter(building_id = i.building_id)
	# # render
	# print('\t\ttttttttttttttttttttttt\n', service_directory_model)
	# return render(request, 'buildings/service_directory.html', service_directory_model)
	cnt = 0
	print(cnt)







