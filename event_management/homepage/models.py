from django.db import models

# Create your models here.
class Reg_User(models.Model):
    Name = models.CharField(max_length=32, null=False)
    Username = models.CharField(max_length=32, null=False)
    Email = models.EmailField(max_length=32, null=False)
    Password= models.CharField(max_length=32, null=False)
    # ConfirmPass= models.CharField(max_length=32, default="")
    interests= models.CharField(max_length=3200, default="")
    Registered_Events = models.CharField(max_length=3200, default="")
    Club_id = models.CharField(max_length=3200, default="")

class Clubs(models.Model):
    clubname=models.CharField(max_length=32)
    image = models.ImageField(null=True, blank=True)
    interests = models.CharField(max_length=3200, default="")
    Events = models.CharField(max_length=3200, default="")
    Blog = models.CharField(max_length=3200, default="")
    Members = models.CharField(max_length=3200, default="")
    Description = models.CharField(max_length=200, default="")


class eve_detail(models.Model):
    Name = models.CharField(max_length=32)
    Club_Name= models.CharField(max_length=32)
    Description=models.CharField(max_length=200)
    UserRegistered = models.CharField(max_length=3200, default="")
    Reviews = models.CharField(max_length=32, default="")
    Reviewedby = models.CharField(max_length=3200, default="")
    Venue = models.CharField(max_length=32, default="")
    poster = models.ImageField(blank=True)
    created_date = models.DateTimeField(blank=True)
    HostSpeakers = models.CharField(null=True, max_length=100)
    interests = models.CharField(max_length=3200, default="")


class tag(models.Model):
    Tag_Name = models.CharField(max_length=32)
    Club_Linked= models.CharField(max_length=3200, default="")
    UserSubscribed=models.CharField(max_length=3200, default="")

