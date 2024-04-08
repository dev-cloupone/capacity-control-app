from .forms import CSVImportForm
from django.shortcuts import render, redirect
from .models import Activity
import csv

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
        return redirect('activities:get_activities')
    else:
        form = CSVImportForm()
    return render(request, 'import_csv_activities.html', {'form': form})

def get_activities(request):
    activity_list = Activity.objects.all()
    return render(
        request,
        'get_activities.html',
        {
            "activityList": activity_list
        }
    )
