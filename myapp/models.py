from django.db import models
from django.contrib import auth

# Create your models here.
class User(auth.models.User):

    def __str__(self):
        return "@{}".format(self.username)
#class Referal(models.Model):

##    refer_by = models.CharField(max_length=25)
    #refer_used_by = models.ForeignKey('auth.User',on_delete='CASCADE',related_name='fo')
class UserResult(models.Model):
    refer_by=models.OneToOneField('auth.User',on_delete='CASCADE',related_name='result')
    point=models.IntegerField()
