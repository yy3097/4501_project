from django import forms
from django.forms import ModelForm
from tracker.models import Sighting

class SquirrelUpdateForm(ModelForm):
    class Meta:
        model = Sighting
        fields = ['longitude', 'latitude', 'squirrel_id', 'shift', 'date', 'age']

class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)