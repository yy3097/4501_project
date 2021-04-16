from django import forms
from django.forms import ModelForm
from tracker.models import Sighting

class UpdateForm(ModelForm):
    class Meta:
        model = Sighting
        fields = ['longitude', 'latitude', 'squirrel_id', 'shift', 'date', 'age']

class AddForm(ModelForm):
    class Meta:
        model = Sighting
        exclude = ['hectare', 'hectare_squirrel_number', 'highlight_fur_color', 'combination', 'color_notes', 'above_ground', 'other_interactions', 'lat_long']
        # fields = ["Latitude", "Longitude", "Unique Squirrel ID", "Shift", "Date", "Age", "Primary Fur Color",
                    # "Location", "Specific Location", "Running", "Chasing", "Climbing", "Eating", "Foraging", "Other Activities", "Kuks",
                    # "Quaas", "Moans", "Tail flags", "Tail twitches", "Approaches", "Indifferent", "Runs from",]

# class NameForm(forms.Form):
#     your_name = forms.CharField(label='Your name', max_length=100)