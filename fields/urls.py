from django.urls import path
from . import views

app_name = 'fields'

urlpatterns = [
    path('import-data/', views.import_data, name='import_data'),
    path('get-fields/', views.get_fields, name='get_fields')
]