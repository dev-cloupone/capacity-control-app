import csv
from .models import Activity
def import_activities( data):

    if data:
        csv_data = data.read().decode('utf-8').splitlines()
        csv_reader = csv.DictReader(csv_data)
        for row in csv_reader:
            size = float(row['Tamanho'].replace('.', '').replace(',', '.'))
            value_activity = float(row['Valor atividade'].replace('.', '').replace(',', '.').replace('R$', ''))
            total_activity = float(row['Total atividade'].replace('.', '').replace(',', '.').replace('R$', ''))

            Activity.objects.create(
                size=size,
                name=row['Atividade'],
                valueActivity=value_activity,
                totalActivity=total_activity
            )