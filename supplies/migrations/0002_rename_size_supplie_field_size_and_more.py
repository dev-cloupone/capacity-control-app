# Generated by Django 5.0.2 on 2024-04-24 14:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('supplies', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='supplie',
            old_name='size',
            new_name='field_size',
        ),
        migrations.RenameField(
            model_name='supplie',
            old_name='sizeSupplie',
            new_name='quantity_per_hectare',
        ),
        migrations.RenameField(
            model_name='supplie',
            old_name='totalSupplie',
            new_name='total',
        ),
        migrations.RenameField(
            model_name='supplie',
            old_name='valueSupplie',
            new_name='value',
        ),
    ]
