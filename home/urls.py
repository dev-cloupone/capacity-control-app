from django.urls import path
from . import views
from users.views import login

urlpatterns = [
    path('import-geral/', views.import_geral, name='import-geral'),
    path('', views.home, name='home'),
    path('fields/get/', views.get_fields, name='get_fields'),
    path('activities/get/', views.get_activities, name='get_activities'),
    path('supplies/get/', views.get_supplies, name='get_supplies'),
    path('users/login/', login, name='login'),

]
