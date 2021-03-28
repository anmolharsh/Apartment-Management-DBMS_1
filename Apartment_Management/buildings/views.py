from django.shortcuts import render,redirect
from .models import Building, Flat, Service_Directory, Occupies

# Create your views here.


def view_main(request):
	# model = Occupies.filter(user = request.user)
	cnt = 0
	return render(request, 'buildings/view_main.html')


def view_flat(request):
	model = Occupies.objects.filter(user_id = request.user.pk)
	flat_model = []
	for i in model:
		temp = Flat.objects.filter(flat_id = str(i.flat_id.pk))
		flat_model.append(temp)
	new_flat_model = []
	for i in flat_model:
		new_flat_model.append(i[0])
	return render(request, 'buildings/flat.html', {'flat_model':new_flat_model})


def view_building(request):
	model = Occupies.objects.filter(user_id = request.user.pk)
	flat_model = []
	for i in model:
		temp = Flat.objects.filter(flat_id = str(i.flat_id.pk))
		flat_model.append(temp)
	new_flat_model = []
	for i in flat_model:
		new_flat_model.append(i[0])
	building_model = []
	for i in new_flat_model:
		temp = Building.objects.filter(building_id = str(i.building_id.pk))
		building_model.append(temp)
	new_building_model = []
	for i in building_model:
		new_building_model.append(i[0])
	new_building_model = set(new_building_model)
	return render(request, 'buildings/building.html', {'flat_model':new_building_model})


def view_service_directory(request):
	model = Occupies.objects.filter(user_id = request.user.pk)
	flat_model = []
	for i in model:
		temp = Flat.objects.filter(flat_id = str(i.flat_id.pk))
		flat_model.append(temp)
	new_flat_model = []
	for i in flat_model:
		new_flat_model.append(i[0])
	building_model = []
	for i in new_flat_model:
		temp = Building.objects.filter(building_id = str(i.building_id.pk))
		building_model.append(temp)
	new_building_model = []
	for i in building_model:
		new_building_model.append(i[0])
	new_building_model = set(new_building_model)
	sd = []
	for i in new_building_model:
		temp = Service_Directory.objects.filter(building_id = i.building_id)
		sd += temp
	new_sd = sd
	return render(request, 'buildings/service_directory.html', {'flat_model':new_sd})







