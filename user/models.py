from django.contrib.auth.models import AbstractUser
from django.db import models
from enquiry.models import City,Center

class CustomUser(AbstractUser):
	ROLES = [('2', 'Counsellor'),('3', 'Student'),('4', 'Trainer')]
	role = models.CharField(max_length=2,choices=ROLES,default='2')
	phone = models.CharField(max_length=10, blank=True)
	select_center = models.ForeignKey(Center,on_delete=models.CASCADE,blank=True,null=True)
	# REQUIRED_FIELDS = ['mobile', 'email']





