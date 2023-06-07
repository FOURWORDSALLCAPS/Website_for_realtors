# Generated by Django 2.2.24 on 2023-06-07 12:29

import phonenumbers
from django.db import migrations
from property.models import Flat


def convert_owners_phone_number(apps, schema_editor):
    all_flats = Flat.objects.all()

    for flat in all_flats:
        phone_number = phonenumbers.parse(flat.owners_phonenumber, "RU")
        if not phonenumbers.is_valid_number(phone_number):
            flat.owner_pure_phone = None
        else:
            normalized_number = phonenumbers.format_number(
                phone_number,
                phonenumbers.PhoneNumberFormat.E164,
            )
            flat.owner_pure_phone = normalized_number
        flat.save()


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0007_flat_owner_pure_phone'),
    ]

    operations = [
        migrations.RunPython(convert_owners_phone_number)
    ]