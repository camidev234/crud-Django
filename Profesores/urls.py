from django.urls import path
from . import views as v

urlpatterns = [
    path('viewAllTeachers/', v.returnsAllTeachers, name='indexTeachers'),
    path('createTeacher/', v.createTeacherView, name='createTeacherView'),
    path('createNewTeacher/', v.createTeacher, name='saveTeacher'),
    path('deleteTeacher/<int:id>', v.deleteTeacher, name='deleteTeacher'),
    path('updateTeacherForm/<int:id>', v.updateTeacherView, name='teacherUpdate'),
    path('updateTeacherSave/<int:id>', v.updateTeacher, name='updateTeacher'),
]