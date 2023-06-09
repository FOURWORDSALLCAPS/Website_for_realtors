# Generated by Django 2.2.24 on 2023-06-08 09:21

from django.db import migrations


def delete_fields_in_flat(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    Flat.objects.all().update(owner='', owner_pure_phone=None, owners_phonenumber='')


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0013_auto_20230609_0952'),
    ]

    operations = [
        migrations.RunPython(delete_fields_in_flat),
        migrations.RemoveField(
            model_name='flat',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='flat',
            name='owner_pure_phone',
        ),
        migrations.RemoveField(
            model_name='flat',
            name='owners_phonenumber',
        ),
    ]
