from django.shortcuts import render, redirect
from .models import Teacher
from .forms import createTeacherForm

# Create your views here.

# function for list teachers on template
def returnsAllTeachers(request):
    teachers = Teacher.objects.all()
    return render(request, 'teachers.html', {
        'teachers': teachers
    })
    
# this function return a form to create new teacher
def createTeacherView(request):
    return render(request, 'createTeacher.html', {
        'formCreate': createTeacherForm()
    })
    
# function save the teacher
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
    
# this function delete teacher on BD 
def deleteTeacher(request, id):
    # get teacher by id
    teacherForDelete = Teacher.objects.get(id=id)
    
    if request.method == 'POST':
        teacherForDelete.delete()
        return redirect('indexTeachers')
    else:
        return redirect('indexTeachers')
    
# return form to update teacher. This function required teacher id
def updateTeacherView(request, id):
    # get teacher by id
    teacherForUpdate = Teacher.objects.get(id=id)
    
    return render(request, 'updateTeacher.html', {
        'teacher': teacherForUpdate
    })

# function save the new information 
def updateTeacher(request, id):
    teacherUpdate = Teacher.objects.get(id=id)
    
    if request.method == 'POST':
        # update rows of this teacher
        teacherUpdate.name = request.POST['name']
        teacherUpdate.lastname = request.POST['lastname']
        teacherUpdate.age = request.POST['age']
        teacherUpdate.email = request.POST['email']
        
        # save the new information on rows.
        teacherUpdate.save()
        
        return redirect('indexTeachers')
    