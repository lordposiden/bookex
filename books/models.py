from django.db import models

# Create your models here.
class Usermodel(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=20)
    user_image = models.ImageField(upload_to='profile_image',null=True,blank=True)