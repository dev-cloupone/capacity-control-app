from django.shortcuts import render, redirect
from .models import ActivityControl
import csv
from django.contrib.auth.decorators import login_required

# @login_required
def get_activitycontrol(request):
    activity_list = ActivityControl.objects.all()
    return render(
        request,
        'get_activitycontrol.html',
        {
            "activityList": activity_list
        }
    )
