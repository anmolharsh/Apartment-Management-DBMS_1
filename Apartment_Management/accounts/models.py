from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User
#from orders.models import Order
#from leave.models import leave_request
from PIL import Image

gender_choices =(
        ('M','M'),
        ('F','F'),
    )

class Resident(models.Model):
    age = models.IntegerField(blank=True,null=True)
    phone = PhoneNumberField(blank=True, help_text='Contact phone number')
    gender = models.CharField(max_length = 1,blank=True,choices = gender_choices)
    user = models.OneToOneField(User, primary_key=True,on_delete=models.CASCADE)
    image = models.ImageField(default='def_M.jpg', upload_to = 'profile_pics')

    def __str__(self):
    	return self.user.username

    def save(self, *args, **kwargs):
        super(Resident, self).save(*args, **kwargs)
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)

class Watchmen(models.Model):
    age = models.IntegerField(blank=True,null=True)
    gender = models.CharField(max_length = 1,blank=True,choices = gender_choices)
    address = models.CharField(max_length=150,blank=True) #update
    phone = PhoneNumberField(blank=True, help_text='Contact phone number') #update
    image = models.ImageField(default='def_M.jpg',blank=True, upload_to = 'profile_pics')
    user = models.OneToOneField(User,primary_key=True,on_delete=models.CASCADE)
    #leave_requests =models.ManyToManyField(leave_request,related_name="leave")

    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        super(Watchmen, self).save(*args, **kwargs)
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)


class Profile(models.Model):
    user = models.OneToOneField(User,primary_key=True,on_delete=models.CASCADE)
    type = models.CharField(max_length=1,default='A')

    def __str__(self):
        return self.user.username