from django.shortcuts import render,redirect
from .models import Building, Flat, Service_Directory, Occupies
from django.contrib.auth.models import User

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
	return render(request, 'buildings/flat.html', {'flat_model':new_flat_model, 'all_flats':Flat.objects.all()})


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
	return render(request, 'buildings/building.html', {'flat_model':Building.objects.all()})


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
	return render(request, 'buildings/service_directory.html', {'flat_model':new_sd, 'all_sd':Service_Directory.objects.all()})



def view_add_occupancy(request):
	context = {'flat': Flat.objects.all() , 'user1': User.objects.all(), 'occupies': Occupies.objects.all() }
	if request.method == 'GET':
		return render(request, 'buildings/add_occupancy.html', context)
	else:
		o = Occupies()
		user_instance = User.objects.get(username = request.POST['user1'])
		o.user_id = user_instance
		flat_instance = Flat.objects.get(flat_id = request.POST['flat'])
		o.flat_id = flat_instance
		o.ownership = request.POST['ownership']
		check = Occupies.objects.filter(flat_id = request.POST['flat'])
		flag = False
		for i in check:
			if i.user_id == user_instance:
				flag = True
		if flag==False:
			o.save()
		return render(request, 'buildings/view_occupancy.html', context)

def view_occupancy(request):
	context = {'occupies': Occupies.objects.all()}
	return render(request, 'buildings/view_occupancy.html', context)


def remove_occupancy(request):
	if request.method == 'POST':
		o = request.POST['o']
		Occupies.objects.get(pk=o).delete()
	return render(request, 'buildings/remove_occupancy.html', {'occupies' : Occupies.objects.all()})


