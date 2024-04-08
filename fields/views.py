from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import CSVImportForm
from .models import Field
import csv

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
            
            return redirect('/fields/get_fields')
    else:
        form = CSVImportForm()
    return render(request, 'import_csv.html', {'form': form})

@login_required
def get_fields(request):
    fieldList = Field.objects.all()
    return render(
        request, 
        'get_fields.html', 
        {
            "fieldList": fieldList
        }
    )
    