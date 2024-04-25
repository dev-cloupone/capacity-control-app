from django.shortcuts import render, redirect
from .models import Activity
import csv
def get_activities(request):
    activity_list = Activity.objects.all()
    return render(
        request,
        'get_activities.html',
        {
            "activityList": activity_list
        }
    )
