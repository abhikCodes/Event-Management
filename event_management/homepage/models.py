from django.db import models

# Create your models here.
class Reg_User(models.Model):
    Name = models.CharField(max_length=32, null=False)
    Username = models.CharField(max_length=32, null=False)
    Email = models.EmailField(max_length=32, null=False)
    Password= models.CharField(max_length=32, null=False)
    # ConfirmPass= models.CharField(max_length=32, default="")
    interests= models.CharField(max_length=3200, default="")

class Clubs(models.Model):
    clubname=models.CharField(max_length=32)

class eve_detail(models.Model):
    Name = models.CharField(max_length=32)
    Club_Name= models.CharField(max_length=32)
    Description=models.CharField(max_length=200)

class tag(models.Model):
	Tag_Name = models.CharField(max_length=32)
