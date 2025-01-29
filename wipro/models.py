from django.db import models

# Create your models here.
class Branch(models.Model):
    name=models.CharField(max_length=30)
    image=models.ImageField(upload_to='image',default='null.jpg')
class saloon(models.Model):
    name1=models.CharField(max_length=20)
    image1=models.ImageField(upload_to='image1',default='null.jpg')
    branch=models.CharField(max_length=50)
class service(models.Model):
    name2=models.CharField(max_length=20)
    image2=models.ImageField(upload_to='image2',default='null.jpg')
    price=models.IntegerField()
    description=models.CharField(max_length=50)
    saloon=models.CharField(max_length=50)