from django.shortcuts import render, get_object_or_404
from tracker.models import Sighting
from django.views.generic.list import ListView
from django.http import HttpResponseBadRequest
from django.http import HttpResponse
from tracker.forms import SquirrelUpdateForm
from django.views.decorators.http import require_http_methods
# Create your views here.

@require_http_methods(['GET'])
def home(request):
    return render(request,'tracker/home.html',{})

@require_http_methods(['GET'])
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

@require_http_methods(['GET', 'POST'])
def update(request, id):
    # print(request)
    if request.method == "POST":
        form = SquirrelUpdateForm(request.POST, instance=get_object_or_404(Sighting,pk=id))
        if form.is_valid():
            # giving an instance keyward arg, f.save() will udpate the model
            form.save()
            # return a pop up that says success
            response = HttpResponse("<script> alert('update succeed!');</script>")
            # print("okay")
            return response
        else:
            pass
            # print("form not valid")
            # print(form)
    else:
        # prepopulated with existing data
        form = SquirrelUpdateForm(instance=get_object_or_404(Sighting, pk=id))

    return render(request, 'tracker/update.html', {'form': form, 'squirrel_id': id})
    



