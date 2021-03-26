from django.db import models
from accounts.models import Resident
# Create your models here.
class Complaints(models.Model) :
	#choice keys
	CREATED = 'CRE'
	IN_PROGRESS = 'PRG'
	COMPLETED = 'CMP'
	status_choices = [
		(CREATED, 'Created'),
		(IN_PROGRESS, 'In Progress'),
		(COMPLETED, 'Completed') 
	]
	complaint_id = models.AutoField(primary_key = True)
	user_id = models.ForeignKey(Resident,on_delete = models.CASCADE)
	status = models.CharField(max_length = 3,choices = status_choices, default = CREATED)
	content = models.TextField(max_length = 200)
	date = models.DateTimeField(auto_now_add = True)
	comments = models.TextField(max_length = 200)

	def __str__(self):
		return str(self.complaint_id)