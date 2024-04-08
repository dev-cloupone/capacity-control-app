from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Field, Activity, Supplie
import csv
from fields.views import import_data, get_fields
from activities.views import import_activities, get_activities
from supplies.views import import_supplies, get_supplies

@login_required
def import_geral(request):
    if request.method == 'POST':
        csv_file = request.FILES.get('csv_file')
        if csv_file:
            campo = request.POST.get('campo')

            if campo == 'fields':
                import_data(csv_file)
                return redirect('/fields/get-fields/')

            elif campo == 'activities':
                import_activities(csv_file)
                return redirect('/activities/get-activities/')

            elif campo == 'supplies':
                import_supplies(csv_file)
                return redirect('/supplies/get-supplies/')

    return render(request, 'import_geral.html')

@login_required
def home(request):
    fields = Field.objects.all().order_by('-size').values()[:10]
    nameList_fields = [field['name'] for field in fields]
    sizeList_fields = [str(field['size']) for field in fields]

    activities = Activity.objects.all().order_by('-size').values()[:10]
    nameList_activities = [activity['name'] for activity in activities]
    valueList_activities = [str(activity['totalActivity']) for activity in activities]

    supplies = Supplie.objects.all().order_by('-size').values()[:10]
    nameList_supplies = [supplie['name'] for supplie in supplies]
    valueList_supplies = [str(supplie['totalSupplie']) for supplie in supplies]

    data = {
        "fields": {
            "categories": nameList_fields,
            "series": [
                {"name": "Fields", "data": sizeList_fields}
            ]
        },
        "activities": {
            "categories": nameList_activities,
            "series": [
                {"name": "Activities", "data": valueList_activities}
            ]
        },
        "supplies": {
            "categories": nameList_supplies,
            "series": [
                {"name": "Supplies", "data": valueList_supplies}
            ]
        }
    }

    return render(request, 'home.html', {'chart_data': data})


