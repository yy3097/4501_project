# Generated by Django 3.2 on 2021-04-15 22:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sighting',
            name='above_ground',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
