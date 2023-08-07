from django.db import models

# Create your models here.

class Employee(models.Model):
    firstname=models.CharField(max_length=100)
    lastname=models.CharField(max_length=100)
    email=models.EmailField()
    experience=models.IntegerField()
