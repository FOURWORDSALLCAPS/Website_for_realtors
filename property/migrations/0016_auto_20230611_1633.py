# Generated by Django 2.2.24 on 2023-06-11 13:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0015_auto_20230609_1032'),
    ]

    operations = [
        migrations.RenameField(
            model_name='owner',
            old_name='owner',
            new_name='full_name',
        ),
    ]