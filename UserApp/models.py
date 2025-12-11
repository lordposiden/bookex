from django.db import models

# Create your models here.
class Usermodel(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    phone = models.CharField(max_length=10)
    address = models.CharField(max_length=200)
    pincode = models.CharField(max_length=6)
    profile_image = models.ImageField(upload_to='profile_image',null=True,blank=True)
