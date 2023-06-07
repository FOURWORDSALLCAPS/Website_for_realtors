# Generated by Django 2.2.24 on 2023-06-07 10:29

from django.db import migrations
from property.models import Flat


def automatically_fill_new_building(apps, schema_editor):
    for flat in Flat.objects.all():
        if flat.construction_year and flat.construction_year >= 2015:
            flat.new_building = True
        else:
            flat.new_building = False
        flat.save()


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0003_flat_new_building'),
    ]

    operations = [
        migrations.RunPython(automatically_fill_new_building)
    ]