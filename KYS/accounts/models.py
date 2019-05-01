from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from phonenumber_field.modelfields import PhoneNumberField
import datetime
# Create your models here.

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE,null=True,blank=True)
	# dob  = models.DateField(null=True,max_length=8)
	phone = models.CharField(null=True,blank=True,max_length=20)
	age = models.IntegerField(null=True)
	# profilePic = models.ImageField(null=True, blank=True)
	# def __str__(self):
	# 	today = date.today()
	# 	age = today.year-dob.year
	# 	if today.month<dob.month or today.month==dob.month and today.day<dob.day:
	# 		age-=1
	# 	return self.age
