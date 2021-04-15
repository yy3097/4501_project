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
            df = pd.DataFrame(sightings.values())
            df.to_csv(path)
        except Exception as e:
            raise e
