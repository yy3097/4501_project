from django.shortcuts import render
from tracker.models import Sighting
from django.views.generic.list import ListView
# Create your views here.

def home(request):
    return render(request,'tracker/home.html',{})

def map(request):
    return render(request, 'tracker/map.html', {'sightings': Sighting.objects.all()[:100]})

class SightingListView(ListView):
    model = Sighting
    paginate_by = 100  # if pagination is desired
    # template_name = 'tracker'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sightings'] = Sighting.objects.all()
        return context
