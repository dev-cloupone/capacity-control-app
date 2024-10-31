import json
import datetime
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.core import serializers
from .models import Partner
import csv
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

@login_required
def get_partner(request):        
    partner_list = Partner.objects.all()
    return render(
        request,
        'get_partner.html',
        {
            "partnerList": partner_list
        }
    )

def crudPartner(request):
    id = request.POST.get('objectId', "0")
    delete = request.POST.get('isDelete', "0")
    if request.method == 'POST':
        if delete == "1":
            print("delete")
            instance = Partner.objects.get(id = id)
            instance.delete()               
        elif  id != "0":
            print("update")
            instance = Partner.objects.get(id = id)
            instance.partnerCode = request.POST['partnerCode']
            instance.description = request.POST['description']
            instance.partnerType = request.POST['partnerType']
            instance.nationalId = request.POST['nationalId']
            instance.address = request.POST['address']
            instance.save()
        else:
            print("new")
            partnerCode = request.POST['partnerCode']
            description = request.POST['description']
            partnerType = request.POST['partnerType']
            nationalId = request.POST['nationalId']
            address = request.POST['address']
            activityModel = Partner(
                partnerCode = partnerCode,
                description = description,
                partnerType = partnerType, 
                nationalId = nationalId, 
                address = address,
                )
            activityModel.save()
    return redirect("/partner/get-partner/")

@csrf_exempt #retirar eventualmente
def getRowData(request):
    departnerCoded_json = json.loads(request.body)
    id = departnerCoded_json["objectId"]
    if  id != "0":
        instance = Partner.objects.get(id = id)
        data = {
        "id": instance.id,
        "partnerCode": instance.partnerCode,
        "description":instance.description,
        "partnerType": instance.partnerType,
        "nationalId":instance.nationalId,
        "address":instance.address
    }
        return JsonResponse(data)
    return HttpResponse(status=404)



        

    

