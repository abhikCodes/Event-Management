from django.db import models
import datetime


# Create your models here.
class Reg_User(models.Model):
    Username = models.CharField(max_length=32)
    Email = models.EmailField(max_length=32)
    Password = models.CharField(max_length=32)
    interests = models.CharField(max_length=3200, default="")
    Registered_Events = models.CharField(max_length=3200, default="")
    # Club_id = models.CharField(max_length=3200, default="")
    cl_id=models.IntegerField(default=0)

class Clubs(models.Model):
    clubname = models.CharField(max_length=32)
    image = models.ImageField(null=True, blank=True)
    interests = models.CharField(max_length=3200, default="")
    Events = models.CharField(max_length=3200, default="")
    Blog = models.CharField(max_length=3200, default="")
    Members = models.CharField(max_length=3200, default="")
    Description = models.CharField(max_length=200)
    oneLiner=models.CharField(max_length=100, default="Snu Club")

class eve_detail(models.Model):
    Name = models.CharField(max_length=32)
    Club_Name = models.CharField(max_length=32)
    Description = models.CharField(max_length=200)
    UserRegistered = models.CharField(max_length=3200, default="")
    Email = models.EmailField(max_length=32)
    Reviews = models.CharField(max_length=32)
    Reviewedby = models.CharField(max_length=3200, default="")
    Venue = models.CharField(max_length=32)
    poster = models.ImageField(blank=True)
    date = models.DateField((u"Conversation Date"), auto_now_add=True, blank=True)
    time = models.TimeField((u"Conversation Time"), auto_now_add=True, blank=True)
    HostSpeakers = models.CharField(null=True, max_length=100)
    interests = models.CharField(max_length=3200, default="")


class tag(models.Model):
    Tag_Name = models.CharField(max_length=32)
    Club_Linked = models.CharField(max_length=3200, default="")
    UserSubscribed = models.CharField(max_length=3200, default="")

