import csv
from .models import Field
import io

def import_fields(data):
    if isinstance(data, str):
        data = io.StringIO(data)
    elif isinstance(data, bytes):
        # Decodifique os bytes em uma string usando utf-8
        data = io.StringIO(data.decode('utf-8'))

    with data as file:
        csv_reader = csv.DictReader(file)

        for row in csv_reader:
            size = row['Hectare'].replace('.', '').replace(',', '.')
            Field.objects.create(
                name=row['Talhão'],
                size=size
            )
