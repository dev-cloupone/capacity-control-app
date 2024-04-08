from django.urls import path
from . import views

app_name = 'activities'

urlpatterns = [
    path('import-activities/', views.import_activities, name='import_activities'),
    path('get-activities/', views.get_activities, name='get_activities')
]