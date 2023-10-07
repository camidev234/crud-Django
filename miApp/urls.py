# importando el path de django para las rutas

from django.urls import path

#importando las funciones de las vistas.
from . import views as v
urlpatterns = [
     #routes here:
     path('index/', v.index),
     path('viewAllProjects/', v.projects, name='viewProjects'),
     path('searchProject/<int:id>', v.projectView),
     path('viewAllTasks/', v.tasks),
     path('createNewProject/', v.createNewProject, name='createProject'),
     path('deleteProject/<int:id>', v.deleteProject, name='deleteProject')
]