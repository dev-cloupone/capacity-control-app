import csv
from .models import ActivityControl
import io
def import_activitycontrol( data):

    if data:
        csv_data = data.read().decode('utf-8').splitlines()
        csv_reader = csv.DictReader(csv_data)
        for row in csv_reader:
            size = float(row['Tamanho'].replace('.', '').replace(',', '.'))
            value = float(row['Valor atividade'].replace('.', '').replace(',', '.').replace('R$', ''))
            total = float(row['Total atividade'].replace('.', '').replace(',', '.').replace('R$', ''))

            ActivityControl.objects.create(
                size=size,
                name=row['Atividade'],
                value=value,
                total=total
            )