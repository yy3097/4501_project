from django.core.management.base import BaseCommand
from tracker.models import Sighting
import csv
import datetime

class Command(BaseCommand): 
    help = 'Import squirrel data from csv file'
    
    def add_arguments(self, parser):
        parser.add_argument('file_path',type=str)
        
    def handle(self, *args, **kwargs): 
        path = kwargs['file_path']
        try: 
            with open(path,encoding='utf-8') as f: 
                squirrel = csv.DictReader(f)
                for row in squirrel: 
                    sighting = Sighting(
                        longitude = row['X'],
                        latitude = row['Y'],
                        squirrel_id = row['Unique Squirrel ID'],
                        hectare = row['Hectare'],                
                        shift = row['Shift'],
                        date = datetime.datetime.strptime(row['Date'],'%m%d%Y'),
                        hectare_squirrel_number = row['Hectare Squirrel Number'],
                        age = row['Age'],
                        primary_fur_color = row['Primary Fur Color'],
                        highlight_fur_color = row['Highlight Fur Color'], 
                        combination = row['Combination of Primary and Highlight Color'],
                        color_notes = row['Color notes'],
                        location = row['Location'],
                        above_ground = row['Above Ground Sighter Measurement'],
                        specific_location = row['Specific Location'],
                        running = (row['Running'].upper() == 'TRUE'),
                        chasing = (row['Chasing'].upper() == 'TRUE'),
                        climbing = (row['Climbing'].upper() == 'TRUE'),
                        eating = (row['Eating'].upper() == 'TRUE'),
                        foraging = (row['Foraging'].upper() == 'TRUE'),
                        other_activities = row['Other Activities'],
                        kuks = (row['Kuks'].upper() == 'TRUE'),
                        quaas = (row['Quaas'].upper() == 'TRUE'),
                        moans = (row['Moans'].upper() == 'TRUE'),
                        tail_flags = (row['Tail flags'].upper() == 'TRUE'),
                        tail_twitches = (row['Tail twitches'].upper() == 'TRUE'),
                        approaches = (row['Approaches'].upper() == 'TRUE'),
                        indifferent = (row['Indifferent'].upper() == 'TRUE'),
                        runs_from = (row['Runs from'].upper() == 'TRUE'),
                        other_interactions = row['Other Interactions'], 
                        lat_long = row['Lat/Long'], 
                    )
                    sighting.save()
            
        except Exception as e: 
            raise e
   

