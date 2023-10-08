from django.shortcuts import render, redirect
from .models import Lounge, Teachers_lounges
from django.http import HttpResponse
from Profesores import models as m
from .forms import createLoungeForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
# Create your views here.



def signUpView(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    
    return render(request, 'signUp.html', {
            'form': form 
        })


def loginUser(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            # Autenticar al usuario
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            
            if user is not None:
                login(request, user)
                return redirect('indexLounge')
    else:
        form = AuthenticationForm()
    
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')       

def indexLounge(request):
    lounges = Lounge.objects.all()
    
    user = request.user
    
    if request.method == 'GET':
        return render(request, 'lounges.html', {
            'lounges': lounges,
            'user': user
        })
    
def createLoungeView(request):
    return render(request, 'createLounge.html', {
        'formCreate': createLoungeForm()
    })
    
    
def createLounge(request):
    if request.method == 'POST':
        Lounge.objects.create(
            lounge_number = request.POST['lounge_number'],
            lounge_description = request.POST['lounge_description'],
            lounge_students = request.POST['lounge_students']
        )
        
        return redirect('indexLounge')
    else: 
        
        return redirect('createLoungeView')
    

def deleteLounge(request, id):
    lounge = Lounge.objects.get(id=id)
    
    if request.method == 'GET':
        lounge.delete()
        return redirect('indexLounge')
    else:
        return redirect('indexLounge')
    
def updateLoungeView(request, id):
    lounge = Lounge.objects.get(id=id)
    
    if request.method == 'POST':
        return render(request, 'updateLounge.html', {
            'loungeUpdate': lounge,
            'formUpdate': createLoungeForm()
        })
        
def updateLounge(request, id):
    lounge = Lounge.objects.get(id=id)
    
    if request.method == 'POST':
        lounge.lounge_number = request.POST['lounge_number']
        lounge.lounge_description = request.POST['lounge_description']
        lounge.lounge_students = request.POST['lounge_students']
        
        lounge.save()
        
        return redirect('indexLounge')
    else:
        return redirect('updateLoungeForm')


def indexLoungesTeachers(request):
    allLoungesTeach = Teachers_lounges.objects.all()
    
    return render(request, 'loungesTeacher.html', {
        'loungesTeachers': allLoungesTeach 
    })
    
def createLoungeTeacherView(request):
    teachers = m.Teacher.objects.all()
    lounges = Lounge.objects.all()
    return render(request, 'asignLt.html', {
        'teachers': teachers,
        'lounges': lounges
    })
    
def assignLounge(request):
    if request.method == 'POST':
        Teachers_lounges.objects.create(
            teacher_id = request.POST['teacher_id'],
            lounge_id = request.POST['lounge_id']
        )
        
        return redirect('indexLt')
    else:
        return redirect('assignLt')
    
def viewTeachersLounges(request, id_lounge):
    teachersLounges = Teachers_lounges.objects.filter(lounge_id=id_lounge)
    lounge = Lounge.objects.get(id=id_lounge)
    teachers = []
    
    for teacherLounge in teachersLounges:
        teachers.append(teacherLounge.teacher)
    
    if request.method == 'GET':
        return render(request, 'teachersLounges.html', {
            'lounges': lounge,
            'teachers': teachers
        })
    else:
        return redirect('indexLt')