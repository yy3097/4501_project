from django.shortcuts import render
from tracker.models import Sighting
# Create your views here.

def home(request):
    return render(request,'tracker/home.html',{})

def map(request):
    sightings = Sighting.objects.all()[:100]
    locs = []
    for sighting in sightings:
        loc = {"longitude": sighting.longitude, "latitude": sighting.latitude}
        locs.append(loc)
    return render(request, 'tracker/map.html', {'sightings': locs})
