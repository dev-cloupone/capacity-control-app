import csv
import io
from .models import Supplie

def import_supplies(data):

    if data:
        if isinstance(data, str):
            data = io.StringIO(data)
        elif isinstance(data, bytes):
            data = io.BytesIO(data)
        csv_reader = csv.DictReader(data)
        for row in csv_reader:
            field_size = float(row['Tamanho'].replace('.', '').replace(',', '.'))
            quantity_per_hectare = float(row['Insumo por hectare'].replace('.', '').replace(',', '.'))
            value = float(row['Valor insumo'].replace('.', '').replace(',', '.').replace('R$', ''))
            total = float(row['Total insumo'].replace('.', '').replace(',', '.').replace('R$', ''))
            Supplie.objects.create(
                name=row['Talhão'],
                field_size=field_size,
                quantity_per_hectare=quantity_per_hectare,
                value=value,
                total=total
            )
