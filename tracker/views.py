from django.shortcuts import render, get_object_or_404
from tracker.models import Sighting
from django.views.generic.list import ListView
from django.http import HttpResponseBadRequest
from django.http import HttpResponse
from tracker.forms import UpdateForm, AddForm
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
        form = UpdateForm(request.POST, instance=get_object_or_404(Sighting,pk=id))
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
        form = UpdateForm(instance=get_object_or_404(Sighting, pk=id))

    return render(request, 'tracker/update.html', {'form': form, 'squirrel_id': id})

@require_http_methods(['GET', 'POST'])
def add(request):
    if request.method == 'POST':
        form = AddForm(request.POST)
        if form.is_valid():
            # looks like form.save() creates a new Sighting obj from form
            new_sighting = form.save()
            # then new_sighting.save() inserts into db
            new_sighting.save()
            response = HttpResponse("<script> alert('insert succeed!');</script>")
            # print("okay")
            return response
    else:
        form = AddForm()

    return render(request, 'tracker/add.html', {'form': form})


def stat(request):
    pass
    



