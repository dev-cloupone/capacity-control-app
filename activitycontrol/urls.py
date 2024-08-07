from django.urls import path
from . import views
from . import import_data

app_name = 'activitycontrol'

urlpatterns = [
    path('get-activitycontrol/', views.get_activitycontrol, name='get_activitycontrol'),
    path('get-activitycontrol/post-crudActivity/', views.crudActivity, name='post_crudActivity'),
    path('get-activitycontrol/get-rowData/', views.getRowData, name='get_rowData'),
    path('get-activitycontrol/get-dayFilterData/', views.get_dayFilterData, name='get_dayFilterData')

]