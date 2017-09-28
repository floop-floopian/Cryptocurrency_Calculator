import datetime
from django.utils import timezone
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
# Create your models here.


class Budget(models.Model):
    amount = models.IntegerField(default=0)

    def __int__(self):
        return self.amount

    
class CPU(models.Model):
    name = models.CharField(max_length=200, unique=True)
    cost = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    def __int__(self):
        return self.cost

    
class RAM(models.Model):
    name = models.CharField(max_length=200, unique=True)
    cost = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    def __int__(self):
        return self.cost

    
class PS(models.Model):
    name = models.CharField(max_length=200, unique=True)
    cost = models.IntegerField(default=0)

    def __str__(self):
        return self.name + self.cost.__str__()


class BitcoinValue(models.Model):
    value = models.FloatField(default=0)

    def __float__(self):
        return self.value


class HashingRate(models.Model):
    hr = models.FloatField(default=0.0)

    def __str__(self):
        return self.hr.__str__()
        

class GPU(models.Model):
    name = models.CharField(max_length=200, unique=True)
    cost = models.IntegerField(default=0)
    hashing_rate = models.OneToOneField(HashingRate, on_delete=models.CASCADE,)
    tdp = models.IntegerField(default=0)

    def __str__(self):
        return self.name + '\n' + self.cost.__str__() + '\n' + self.hashing_rate.__str__() + '\n' + self.tdp.__str__()

