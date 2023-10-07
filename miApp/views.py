from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import Project, Task
from .forms import ProjectForm
# Create your views here.


def index(request):
    return render(request, 'index.html')

def projects(request):
    allProys = Project.objects.all()
    prs = list(Project.objects.values())
    # return data on html
    return render(request, 'projects.html', {
        'proyectos': allProys,
        'form': ProjectForm()
    })

def projectView(request, id):
    project = Project.objects.get(id=id)
    return HttpResponse('project: %s' %project.name)

def tasks(request):
    tasks = Task.objects.all()
    return render(request, 'tasks.html', {
        'tareas': tasks
    })
    
    
def createNewProject(request):
    allProys = Project.objects.all()
    if request.method == 'GET':
        return render(request, 'projects.html', {
        'proyectos': allProys,
        'form': ProjectForm()
        })
    else:
        Project.objects.create(name=request.POST['name'])
        return redirect('viewProjects')
    
def deleteProject(request, id):
    projectForDelete = Project.objects.get(id=id)
    if request.method == 'POST':
        projectForDelete.delete()
        return redirect('viewProjects')
    
    return redirect('viewProjects')
    