from django.forms import ModelForm
from .models import Sighting

class AddSightingForm(ModelForm):
    class Meta:
        model = Sighting
        fields = '__all__'

class EditSightingForm(ModelForm):
    class Meta:
        model = Sighting
        fields = [
            'longitude',
            'latitude',
            'squirrel_id',
            'shift',
            'date',
            'age'
        ]
