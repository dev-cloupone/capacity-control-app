from django.urls import path
from . import views
from . import import_data

app_name = 'partner'

urlpatterns = [
    path('get-partner/', views.get_partner, name='get_partner'),
    path('get-partner/post-crudPartner/', views.crudPartner, name='post_crudPartner'),
    path('get-partner/get-rowData/', views.getRowData, name='get_rowData'),

]