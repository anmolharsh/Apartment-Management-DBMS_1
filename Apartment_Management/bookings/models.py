from django.db import models

from accounts.models import Resident
# Create your models here.
class Booking(models.Model) :
	WAITING = 'WAIT'
	ALLOTTED = 'ALOT'
	REJECTED = 'REJC'
	status_choices = [
		(WAITING, 'WAITING FOR APPROVAL'),
		(ALLOTTED, 'ALLOTTED'),
		(REJECTED, 'REJECTED'),
	]

	BADMINTON = 'BADM'
	TABLE_TENNIS = 'TATE'
	TENNIS = 'TENS'
	COMMUNITY_HALL = 'COMH'
	facility_choices = [
		(BADMINTON,'Badminton'),
		(TABLE_TENNIS, 'Table Tennis'),
		(TENNIS, 'Tennis'),
		(COMMUNITY_HALL, 'Community Hall'),
	]

	booking_id = models.AutoField(primary_key = True)
	user_id = models.ForeignKey(Resident,on_delete = models.CASCADE)
	facility = models.CharField(max_length = 20, choices = facility_choices)
	status = models.CharField(max_length = 4,choices = status_choices, default = WAITING)
	check_in = models.DateTimeField()
	duration = models.IntegerField()
	check_out = models.DateTimeField(null = True)