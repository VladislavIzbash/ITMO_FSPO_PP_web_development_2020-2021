from django.db import models
from django.contrib.auth.models import AbstractUser


class Car(models.Model):
    number = models.CharField(max_length=15)
    brand = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    color = models.CharField(max_length=30)

    def __str__(self):
        return self.number


class CarOwner(AbstractUser):
    passport = models.CharField(max_length=10)
    address = models.CharField(max_length=200)
    nationality = models.CharField(max_length=100)
    birth_date = models.DateTimeField(null=True)
    cars = models.ManyToManyField(Car, through='Ownership')
    
    def __str__(self):
        return f'{self.first_name} {self.last_name} ({self.username})'
    

class Ownership(models.Model):
    owner = models.ForeignKey(CarOwner, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    start_date = models.DateTimeField
    end_date = models.DateTimeField(null=True)

    def __str__(self):
        return f'{self.owner} - {self.car}'
    

class DriverLicense(models.Model):
    driver = models.ForeignKey(CarOwner, on_delete=models.CASCADE)
    number = models.CharField(max_length=10)
    type = models.CharField(max_length=10)
    date = models.DateTimeField

    def __str__(self):
        return self.number
    

