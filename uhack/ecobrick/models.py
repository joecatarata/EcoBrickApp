from django.db import models
from django.contrib.auth.models import User



class Brick(models.Model):
    #brick details
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    brickWeight = models.PositiveIntegerField(default = 0)
    brickVolume = models.PositiveIntegerField(default = 0)
    brickPoint = models.PositiveIntegerField(default = 0)

class Reward(models.Model):
    #reward details

    rewardName = models.CharField(max_length = 250)
    pointCost = models.PositiveIntegerField(default = 0)
    description = models.CharField(max_length = 1000)

    def __str__(self):
        return str(self.rewardName)

# Create your models here.
class UserDetail(models.Model):
    #user details
    email = models.EmailField(max_length = 50, unique = True, blank = False, null = True)
    firstName = models.CharField(max_length = 50)
    lastName = models.CharField(max_length = 50)
    address = models.CharField(max_length = 150)
    contactNum = models.CharField(max_length = 50)
    brickNum = models.PositiveIntegerField(default = 0)
    brickWeight = models.PositiveIntegerField(default = 0)
    brickPoints = models.PositiveIntegerField(default = 0)
    #user account type
    choices = ((0, 'Staff'), (1, 'Regular User'))
    userType = models.IntegerField(default = 1, choices = choices)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.username
class MyReward(models.Model):
    user = models.ForeignKey(UserDetail, on_delete=models.CASCADE)
    rewardName = models.CharField(max_length = 250)
    pointCost = models.PositiveIntegerField(default = 0)
    description = models.CharField(max_length = 1000)

    # def __str__(self):
    #     return str(rewardName)
class Partner(models.Model):
    #partner details
    region = models.CharField(max_length = 100)
    city = models.CharField(max_length = 100)
    barangay = models.CharField(max_length = 100)
    lat = models.DecimalField(default = 0, decimal_places = 10, max_digits=15)
    long = models.DecimalField(default = 0, decimal_places = 10, max_digits=15)
    contactNum = models.CharField(max_length = 50)
