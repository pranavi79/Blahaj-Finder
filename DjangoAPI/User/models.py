from django.db import models

# Create your models here.

class Blahaj(models.Model):
    BlahajId = models.AutoField(primary_key=True)
    BlahajName = models.CharField(max_length=500)

class Users(models.Model):
    UsersId = models.AutoField(primary_key=True)
    UsersName = models.CharField(max_length=500)
    Blahaj = models.CharField(max_length=500)
    DateOfJoining = models.DateField()
    PhotoFileName = models.CharField(max_length=500)