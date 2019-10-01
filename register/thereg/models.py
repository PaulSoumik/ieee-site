from django.db import models
from django.contrib.auth.models import User
from django import forms
# Create your models here.
YEAR = [('1st','first'),('2nd','second'),('3rd','third'),('4th','fourth'),('HS or Lower','HS or Lower'),('grad','Graduate'),('PG','Post-Graduate')]

class UserProfileInfo(models.Model):
	user = models.OneToOneField(User,on_delete=models.CASCADE)
	Institute = models.CharField(max_length=200,blank=True)
	Department = models.CharField(max_length=200,blank=True)
	Year = models.CharField(max_length=13,choices=YEAR)
	profile_pic = models.ImageField(upload_to='profile_pics',blank=True)
	def __str__(self):
		return self.user.username

