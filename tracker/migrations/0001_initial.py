# Generated by Django 3.2 on 2021-04-15 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sighting',
            fields=[
                ('longitude', models.FloatField()),
                ('latitude', models.FloatField()),
                ('squirrel_id', models.CharField(max_length=15, primary_key=True, serialize=False, unique=True)),
                ('hectare', models.CharField(max_length=5)),
                ('shift', models.CharField(choices=[('AM', 'AM'), ('PM', 'PM')], max_length=5)),
                ('date', models.DateField()),
                ('hectare_squirrel_number', models.IntegerField(null=True)),
                ('age', models.CharField(blank=True, choices=[('Adult', 'Adult'), ('Juvenile', 'Juvenile')], max_length=10)),
                ('primary_fur_color', models.CharField(blank=True, choices=[('Gray', 'Gray'), ('Cinnamon', 'Cinnamon'), ('Black', 'Black')], max_length=10)),
                ('highlight_fur_color', models.CharField(blank=True, max_length=50)),
                ('combination', models.CharField(blank=True, max_length=50)),
                ('color_notes', models.CharField(blank=True, max_length=100)),
                ('location', models.CharField(blank=True, choices=[('Above Ground', 'Above Ground'), ('Ground Plane', 'Ground Plane')], max_length=20)),
                ('above_ground', models.IntegerField(blank=True, null=True)),
                ('specific_location', models.CharField(blank=True, max_length=100)),
                ('running', models.BooleanField(blank=True)),
                ('chasing', models.BooleanField(blank=True)),
                ('climbing', models.BooleanField(blank=True)),
                ('eating', models.BooleanField(blank=True)),
                ('foraging', models.BooleanField(blank=True)),
                ('other_activities', models.CharField(blank=True, max_length=100)),
                ('kuks', models.BooleanField(blank=True)),
                ('quaas', models.BooleanField(blank=True)),
                ('moans', models.BooleanField(blank=True)),
                ('tail_flags', models.BooleanField(blank=True)),
                ('tail_twitches', models.BooleanField(blank=True)),
                ('approaches', models.BooleanField(blank=True)),
                ('indifferent', models.BooleanField(blank=True)),
                ('runs_from', models.BooleanField(blank=True)),
                ('other_interactions', models.CharField(blank=True, max_length=100)),
                ('lat_long', models.CharField(max_length=100)),
            ],
        ),
    ]
