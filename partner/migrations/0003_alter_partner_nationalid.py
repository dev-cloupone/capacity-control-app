# Generated by Django 5.1.1 on 2024-10-29 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partner', '0002_rename_code_partner_partnercode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partner',
            name='nationalId',
            field=models.CharField(max_length=20),
        ),
    ]