from django.urls import path
from . import views
from . import import_data

app_name = 'activitycontrol'

urlpatterns = [
    path('get-activitycontrol/', views.get_activitycontrol, name='get_activitycontrol')
]