from django.db import models
from Profesores import models as m
# Create your models here.


#creating model project here
class Project(models.Model):
    #rowName = models.DataType(lenght)
    name = models.CharField(max_length=255)
    
# projects = ['Learn Django', 'learn Laravel', 'Develop app', 'Win SENAsoft']
    
# for project in range(4):
#     new_project = Project(name=projects[project])
#     new_project.save()
    

class Task(models.Model):
    #normal rows of model tasks
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=300)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
  
