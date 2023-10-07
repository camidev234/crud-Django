from django.shortcuts import render, redirect
from .models import Teacher
from .forms import createTeacherForm

# Create your views here.

def returnsAllTeachers(request):
    teachers = Teacher.objects.all()
    return render(request, 'teachers.html', {
        'teachers': teachers
    })
    

def createTeacherView(request):
    return render(request, 'createTeacher.html', {
        'formCreate': createTeacherForm()
    })
    
def createTeacher(request):
    if request.method == 'POST':
        Teacher.objects.create(
            name=request.POST['name'],
            lastname = request.POST['lastname'],
            age = request.POST['age'],
            email = request.POST['email']
        )
        return redirect('indexTeachers')
    else:
        return redirect('indexTeachers')
    
    
def deleteTeacher(request, id):
    teacherForDelete = Teacher.objects.get(id=id)
    
    if request.method == 'POST':
        teacherForDelete.delete()
        return redirect('indexTeachers')
    else:
        return redirect('indexTeachers')
    
def updateTeacherView(request, id):
    teacherForUpdate = Teacher.objects.get(id=id)
    
    return render(request, 'updateTeacher.html', {
        'teacher': teacherForUpdate
    })

def updateTeacher(request, id):
    teacherUpdate = Teacher.objects.get(id=id)
    
    if request.method == 'POST':
        teacherUpdate.name = request.POST['name']
        teacherUpdate.lastname = request.POST['lastname']
        teacherUpdate.age = request.POST['age']
        teacherUpdate.email = request.POST['email']
        
        teacherUpdate.save()
        
        return redirect('indexTeachers')