import csv
from .models import Field
def import_fields (data):

    if isinstance(data, str):
        data = io.StringIO(data)
    elif isinstance(data, bytes):
        data = io.BytesIO(data)
        csv_reader = csv.DictReader(csv_data)
        for row in csv_reader:
            size = row['Hectare'].replace('.', '').replace(',', '.')
            Field.objects.create(
                name=row['Talhão'],
                size=size
            )
