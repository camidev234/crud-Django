from django.db import models
from Profesores import models as m
# Create your models here.


class Lounge(models.Model):
    lounge_number = models.CharField(max_length=100)
    lounge_description = models.CharField(max_length=300)
    lounge_students = models.IntegerField()


class Teachers_lounges(models.Model):
    teacher = models.ForeignKey(m.Teacher, on_delete=models.CASCADE)
    lounge = models.ForeignKey(Lounge, on_delete=models.CASCADE)