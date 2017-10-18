from django.db import models

# Create your models here.
class Reg_User(models.Model):
    Username = models.CharField(max_length=32)
    Email = models.EmailField(max_length=32)
    Password= models.CharField(max_length=32)
 
class Clubs(models.Model):
    clubname=models.CharField(max_length=32)
