import datetime
from django.utils import timezone
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
# Create your models here.
bdgt = 0
checkcost = 0

class Budget(models.Model):
    amount = models.IntegerField(default=0)

    def __int__(self):
        return self.amount

    
class CPU(models.Model):
    name = models.CharField(max_length=200, unique=True)
    cost = models.IntegerField(default=0)

    def __int__(self):
        return self.cost

    def __str__(self):
        return self.name + '\n' + self.cost.__str__()

    
class RAM(models.Model):
    name = models.CharField(max_length=200, unique=True)
    cost = models.IntegerField(default=0)

    def __int__(self):
        return self.cost

    def __str__(self):
        return self.name + '\n' + self.cost.__str__()

    
class PS(models.Model):
    name = models.CharField(max_length=200, unique=True)
    cost = models.IntegerField(default=0)

    def __str__(self):
        return self.name + self.cost.__str__()


class GPU(models.Model):
    name = models.CharField(max_length=200, unique=True)
    cost = models.IntegerField(default=0)
    hashing_rate = models.FloatField(default=0)
    tdp = models.IntegerField(default=0)

    def __str__(self):
        return self.name + '\n' + self.cost.__str__() + '\n' + self.hashing_rate.__str__() + '\n' + self.tdp.__str__()
