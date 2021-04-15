from django.core.management.base import BaseCommand
from tracker.models import Sighting
import csv
import pandas as pd

class Command(BaseCommand):
    help = 'Export squirrel data to csv file'
    
    def add_arguments(self, parser):
        parser.add_argument('file_path',type=str)
        
    def handle(self, *args, **kwargs):
        path = kwargs['file_path']
        try:
            sightings = Sighting.objects.all()
            columns = ['X','Y','Unique Squirrel ID','Hectare','Shift','Date','Hectare Squirrel Number','Age',
                       'Primary Fur Color','Highlight Fur Color','Combination of Primary and Highlight Color',
                       'Color notes','Location','Above Ground Sighter Measurement','Specific Location','Running',
                       'Chasing','Climbing','Eating','Foraging','Other Activities','Kuks','Quaas','Moans',
                       'Tail flags','Tail twitches','Approaches','Indifferent','Runs from','Other Interactions',
                       'Lat/Long']
            df = pd.DataFrame(sightings.values())
            df.columns = columns
            df.to_csv(path)
        except Exception as e:
            raise e
