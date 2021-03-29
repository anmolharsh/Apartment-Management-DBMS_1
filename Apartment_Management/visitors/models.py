from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from accounts.models import Resident

# Create your models here.
class Visitor(models.Model) :
	WAITING = 'WAIT'
	APPROVED = 'APRV'
	REJECTED = 'REJC'
	status_choices = [
		(WAITING, 'WAITING FOR APPROVAL'),
		(APPROVED, 'APPROVED'),
		(REJECTED, 'REJECTED'),
	]
	visitor_id = models.AutoField(primary_key = True)
	user_id = models.ForeignKey(Resident,on_delete = models.CASCADE)
	fname = models.CharField(max_length = 20)
	lname = models.CharField(max_length = 20, null = True)
	status = models.CharField(max_length = 4,choices = status_choices, null = True)
	phone = PhoneNumberField(blank=True, help_text='Contact phone number')
	datetime_entry = models.DateTimeField(null = True)
	datetime_exit = models.DateTimeField(null = True)
	
	def __str__(self):
		return str(self.fname)