# Generated by Django 5.1.1 on 2024-10-29 18:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('partner', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='partner',
            old_name='code',
            new_name='partnerCode',
        ),
    ]
