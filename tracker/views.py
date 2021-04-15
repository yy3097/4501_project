from django.shortcuts import render
from tracker.models import Sighting
# Create your views here.

def home(request):
    return render(request,'tracker/home.html',{})

def map(request):
    return render(request, 'tracker/map.html', {'sightings': Sighting.objects.all()[:100]})
