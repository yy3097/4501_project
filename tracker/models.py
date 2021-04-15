from django.db import models
from django.utils.translation import gettext as _

class Sighting(models.Model): 
    longitude = models.FloatField(
        blank = False,
    )
    
    latitude = models.FloatField(
        blank = False,
    )
    
    squirrel_id= models.CharField(
        max_length = 15,
        blank = False,
        unique = True,
        primary_key = True
    )
    
    hectare = models.CharField(
        max_length = 5
    )
    
    AM='AM'
    PM='PM'
    SHIFT_ = [
        (AM,_('AM')),
        (PM,_('PM')),
    ]
    shift = models.CharField(
        max_length = 5,
        choices = SHIFT_,
    )

    date = models.DateField()

    hectare_squirrel_number = models.IntegerField(
        null=True
    )

    ADULT = 'Adult'
    JUVENILE = 'Juvenile'
    AGE_ = [
        (ADULT,_('Adult')),
        (JUVENILE,_('Juvenile')),
    ]
    age = models.CharField(
        max_length = 10,
        choices = AGE_,
        blank = True,
    )

    GRAY= 'Gray'
    CINNAMON= 'Cinnamon'
    BLACK = 'Black'
    COLOR = [
        (GRAY,_('Gray')),
        (CINNAMON,_('Cinnamon')),
        (BLACK,_('Black')),
    ]
    primary_fur_color = models.CharField(
        max_length = 10,
        choices = COLOR,
        blank = True,
    )

    highlight_fur_color = models.CharField(
        max_length = 50,
        blank = True
    )

    combination = models.CharField(
        max_length = 50,
        blank = True
    )

    color_notes = models.CharField(
        max_length = 100,
        blank = True,
    )

    ABOVE_GROUND = 'Above Ground'
    GROUND_PLANE = 'Ground Plane'
    LOCATION_ = [
        (ABOVE_GROUND, _('Above Ground')),
        (GROUND_PLANE, _('Ground Plane')),
    ]
    location = models.CharField(
        max_length = 20,
        choices = LOCATION_,
        blank = True,
    )

    above_ground = models.IntegerField(
        blank = True,
        null = True,
    )

    specific_location = models.CharField(
        max_length = 100,
        blank = True,
    )

    running = models.BooleanField(
        blank = True,
    )

    chasing = models.BooleanField(
        blank = True,
    )

    climbing = models.BooleanField(
        blank = True,
    )

    eating = models.BooleanField(
        blank = True,
    )

    foraging = models.BooleanField(
        blank = True,
    )

    other_activities = models.CharField(
        max_length = 100,
        blank = True,
    )

    kuks = models.BooleanField(
        blank = True,
    )

    quaas = models.BooleanField(
        blank = True,
    )

    moans = models.BooleanField(
        blank = True,
    )

    tail_flags = models.BooleanField(
        blank = True,
    )

    tail_twitches = models.BooleanField(
        blank = True,
    )

    approaches = models.BooleanField(
        blank = True,
    )

    indifferent = models.BooleanField(
        blank = True,
    )

    runs_from = models.BooleanField(
        blank = True,
    )

    other_interactions = models.CharField(
        max_length = 100,
        blank = True,
    )

    lat_long = models.CharField(
        max_length = 100,
    )

    def __str__(self):
        return self.squirrel_id



# Create your models here.
