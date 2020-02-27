from django.conf import settings
from django.db import models

# Create your models here.

class Car(models.Model):
	name_auto = models.CharField(max_length = 50, default="")
	model_auto = models.CharField(max_length = 100, default="")
	year = models.IntegerField(default = 0)
	color = models.CharField(max_length = 50, default="")
	lenght = models.CharField(max_length = 15, default="")
	height = models.CharField(max_length = 15, default="")
	width = models.CharField(max_length = 15, default="")
	clearance = models.CharField(max_length = 15, default="")

	def __str__(self):
		return (str(self.model_auto) + ' ' + str(self.year))