# Generated by Django 5.0.2 on 2024-03-20 18:39

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('size', models.FloatField()),
                ('valueActivity', models.FloatField()),
                ('totalActivity', models.FloatField()),
            ],
        ),
    ]
