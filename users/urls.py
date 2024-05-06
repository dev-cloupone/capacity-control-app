from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import CustomPasswordChangeView


app_name = 'users'

urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('user-settings/', views.user_settings, name='user_settings'),
    #path('alterar-senha/user-settings', views.alterar_senha, name='alterar_senha'),
    path('password_change/', CustomPasswordChangeView.as_view(template_name='password_change_form.html'),
         name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='password_change_done.html'),
         name='password_change_done')
]