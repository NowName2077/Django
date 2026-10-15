from django.contrib.auth.models import User
from django.db import models

# Create your models here.

#class Roles(models.Model):
class UserProfile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )
    def __str__(self):
        return str('User'+' '+self.user.username)
#class Team(models.Model):
#    name = models.CharField(max_length=100)
#    sport = models.CharField(max_length=100)
#    players = models.ManyToManyField(Users)
#class Match(models.Model):
#    date = models.DateField()
#    opponent = models.CharField(max_length=100)
#    result = models.CharField(max_length=50, blank=True)
#    venue = models.CharField(max_length=200)
#class TrainingSession(models.Model):
#    date = models.DateField()