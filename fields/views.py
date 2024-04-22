from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import CSVImportForm
from .models import Field
import csv
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
    