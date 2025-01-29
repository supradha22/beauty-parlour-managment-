from django.db import models
from wipro.models import*
# Create your models here.
class registering(models.Model):
    name=models.CharField(max_length=30)
    number=models.IntegerField()
    password=models.CharField(max_length=30)
    email=models.CharField(max_length=20)
class contact(models.Model):
      name1=models.CharField(max_length=20,default="default")
      email1=models.CharField(max_length=25,default="default")
      message=models.CharField(max_length=20,default="default")
class booking(models.Model):
     userreg =models.ForeignKey(registering,on_delete=models.CASCADE)
     userser =models.ForeignKey(service,on_delete=models.CASCADE)
     bookingdate =models.CharField(max_length=20)
     bookingtime =models.CharField(max_length=20)
     status=models.IntegerField(default=0)