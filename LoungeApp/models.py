from django.db import models

# Create your models here.


class Lounge(models.Model):
    lounge_number = models.CharField(max_length=100)
    lounge_description = models.CharField(max_length=300)
    lounge_students = models.IntegerField()
    