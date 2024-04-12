import csv
from .models import Field


def import_data (data):
    if data:
        csv_data = data.read().decode('utf-8').splitlines()
        csv_reader = csv.DictReader(csv_data)
        for row in csv_reader:
            size = row['Hectare'].replace('.', '').replace(',', '.')
            Field.objects.create(
                name=row['Talhão'],
                size=size
            )
