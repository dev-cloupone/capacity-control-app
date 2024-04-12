from django.urls import path
from . import views
from . import import_data

app_name = 'activities'

urlpatterns = [
    path('import-activities/', import_data.import_activities, name='import_activities'),
    path('get-activities/', views.get_activities, name='get_activities')
]