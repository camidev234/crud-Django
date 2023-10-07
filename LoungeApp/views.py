from django.shortcuts import render
from .models import Lounge
# Create your views here.

def indexLounge(request):
    lounges = Lounge.objects.all()
    return render(request, 'lounges.html', {
        'lounges': lounges
    })


