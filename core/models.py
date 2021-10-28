from django.db import models

# Create your models here.

class MyBirthDay(models.Model):
	name=models.CharField(max_length=200)
	birthday=models.DateField()

	def __str__(self):
		return self.name