import json
import datetime
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.core import serializers
from .models import ActivityControl
import csv
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

@login_required
def get_activitycontrol(request):        
    activity_list = ActivityControl.objects.filter(date=datetime.date.today())
    print(activity_list)
    return render(
        request,
        'get_activitycontrol.html',
        {
            "activityList": activity_list
        }
    )

def crudActivity(request):
    id = request.POST.get('objectId', "0")
    delete = request.POST.get('isDelete', "0")
    if request.method == 'POST':
        if delete == "1":
            print("delete")
            instance = ActivityControl.objects.get(id = id)
            instance.delete()               
        elif  id != "0":
            print("update")
            instance = ActivityControl.objects.get(id = id)
            instance.dateStart = request.POST['dateStart']
            instance.dateEnd = request.POST['dateEnd']
            instance.activity = request.POST['activity']
            instance.description = request.POST['description']
            instance.save()
        else:
            print("new")
            user = request.user
            date = request.POST['insertDate']
            dateStart = request.POST['dateStart']
            dateEnd = request.POST['dateEnd']
            activity = request.POST['activity']
            description = request.POST['description']
            activityModel = ActivityControl(
                user = user,
                date = date,
                dateStart = dateStart, 
                dateEnd = dateEnd,
                activity = activity, 
                description = description,
                total = 8
                )
            activityModel.save()
    return redirect("/activitycontrol/get-activitycontrol/")

@csrf_exempt #retirar eventualmente
def getRowData(request):
    decoded_json = json.loads(request.body)
    id = decoded_json["objectId"]
    if  id != "0":
        instance = ActivityControl.objects.get(id = id)
        data = {
        "id": instance.id,
        "dateStart": instance.dateStart,
        "dateEnd": instance.dateEnd,
        "activity":instance.activity,
        "description":instance.description
        # Add other fields you need
    }
        return JsonResponse(data)
    return HttpResponse(status=404)

@csrf_exempt #retirar eventualmente
def get_dayFilterData(request):
    decoded_json = json.loads(request.body)
    day = decoded_json["day"]     
    month = decoded_json["month"]     
    year = decoded_json["year"] 
    date = datetime.date(year, month, day)
    activity_list = ActivityControl.objects.filter(date=date)
    print(activity_list)
    data = serializers.serialize('json', activity_list)
    return HttpResponse(data, content_type="application/json")



        

    

