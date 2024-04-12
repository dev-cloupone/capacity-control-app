from django.urls import path
from . import views
from . import import_data

app_name = 'supplies'

urlpatterns = [
    path('import-supplies/', import_data.import_supplies, name='import_supplies'),
    path('get-supplies/', views.get_supplies, name='get_supplies')
]