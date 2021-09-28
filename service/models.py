from django.db import models

# Create your models here.

class Aplication(models.Model):
	"""docstring for Aplication"""
	name = models.CharField(max_length=100)
	phone_number = models.CharField(max_length=10)
	house_number = models.CharField(max_length=5)
	problem = models.CharField(max_length=300)

	# When the worker completed the request - true
	completed = models.BooleanField(default=0) 
	worker = models.ForeignKey('Worker', on_delete=models.CASCADE)

class Worker(models.Model):
	"""docstring for Worker"""

	# Data of worker
	first_name = models.CharField(max_length=50)
	second_name = models.CharField(max_length=50)
	phone_number = models.CharField(max_length=10)

	# Data for logining
	login = models.CharField(max_length=10)
	password = models.CharField(max_length=20)


class House(models.Model):
	"""docstring for House"""

	number = models.CharField(max_length=5)
	worker = models.ForeignKey('Worker', on_delete=models.CASCADE)
	
		

		


