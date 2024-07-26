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

def crudActivity(request):
    if request.method == 'POST':
        id = request.POST['objectId']
        if id:
            instance = ActivityControl.objects.get(id = id)
            dateStart = request.POST['dateStart']
            dateEnd = request.POST['dateEnd']
            activity = request.POST['activity']
            description = request.POST['description']
            activityModel = ActivityControl(
                dateStart = dateStart, 
                dateEnd = dateEnd,
                activity = activity, 
                description = description,
                total = 8
                )
            activityModel.save()        
        activity_list = ActivityControl.objects.all()
        return render(
        request,
        'get_activitycontrol.html',
        {
            "activityList": activity_list
        }
    )
