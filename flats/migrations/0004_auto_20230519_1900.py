# Generated by Django 3.2 on 2023-05-19 16:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flats', '0003_category_flat_object'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Flat',
        ),
        migrations.DeleteModel(
            name='Object',
        ),
    ]
