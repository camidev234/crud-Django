from django.shortcuts import render, redirect
from .models import Lounge
from .forms import createLoungeForm
# Create your views here.

def indexLounge(request):
    lounges = Lounge.objects.all()
    return render(request, 'lounges.html', {
        'lounges': lounges
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
