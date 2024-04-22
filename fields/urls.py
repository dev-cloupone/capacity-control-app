from django.urls import path
from . import views
from . import import_data

app_name = 'fields'

urlpatterns = [
    path('get-fields/', views.get_fields, name='get_fields')
]