from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Supplie
import csv
@login_required
def get_supplies(request):
    supplie_list = Supplie.objects.all()
    return render(
        request,
        'get_supplies.html',
        {
            "supplieList": supplie_list
        }
    )