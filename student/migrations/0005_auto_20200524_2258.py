# Generated by Django 3.0.4 on 2020-05-24 20:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0004_auto_20200522_1733'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='Living_area',
            new_name='living_area',
        ),
    ]
