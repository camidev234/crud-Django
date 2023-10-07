from django.db import models

# Create your models here.

class Teacher(models.Model):
    name = models.CharField(max_length=300)
    lastname = models.CharField(max_length=200)
    age = models.IntegerField(max_length=3)
    email = models.CharField(max_length=300)
    