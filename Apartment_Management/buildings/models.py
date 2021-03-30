from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
flat_type_choices = ( ('1','1'), ('2','2'), ('3','3'), ('4','4'), ('5','5') )
ownership_choices = ( ('Tenant','Tenant'), ('Owner','Owner') )

class Building(models.Model):
	building_id = models.CharField(max_length=10, primary_key=True)
	building_name = models.CharField(max_length=30)
	n_floors = models.IntegerField(default=0)
	n_flats = models.IntegerField(default=0)

class Flat(models.Model):
	flat_id = models.CharField(max_length=10, primary_key=True)
	flat_no = models.CharField(max_length=20)
	flat_type = models.IntegerField()
	flat_area = models.IntegerField(default=0)
	vaccancy = models.IntegerField(default=0)
	building_id = models.ForeignKey(Building, on_delete=models.CASCADE)


class Service_Directory(models.Model):
	service_id = models.CharField(max_length=10, primary_key=True)
	name = models.CharField(max_length=50)
	profession = models.CharField(max_length=30)
	building_id = models.ForeignKey(Building, on_delete=models.CASCADE)
	phone_no = PhoneNumberField(blank=False)

class Occupies(models.Model):
	flat_id = models.ForeignKey(Flat, on_delete=models.CASCADE)
	user_id = models.ForeignKey(User, on_delete=models.CASCADE)
	ownership = models.CharField(max_length=10, choices=ownership_choices)
