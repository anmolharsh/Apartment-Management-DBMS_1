from django.db import models
from accounts.models import Resident
from django_extensions.db import fields as extension_fields
from django.urls import reverse
from django_extensions.db.fields import AutoSlugField
# Create your models here.
class Notice(models.Model) :
	
	title = models.CharField(max_length = 40)
	slug = extension_fields.AutoSlugField(populate_from='title', blank=True)
	date = models.DateTimeField( auto_now = True)
	content = models.TextField(max_length = 400)
	link = models.URLField(max_length=200,blank= True, null = True)

	def __str__(self):
		return str(self.title)

	def get_absolute_url(self):
		return reverse('noticeboard_notice_detail', args=(self.slug,))

	def get_update_url(self):
		return reverse('noticeboard_notice_update', args=(self.slug,))

	def get_delete_url(self):
		return reverse('noticeboard_notice_delete', args=(self.slug,))
