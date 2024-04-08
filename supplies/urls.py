from django.urls import path
from . import views

app_name = 'supplies'

urlpatterns = [
    path('import-supplies/', views.import_supplies, name='import_supplies'),
    path('get-supplies/', views.get_supplies, name='get_supplies')
]