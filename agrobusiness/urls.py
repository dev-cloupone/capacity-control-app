from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.core.mail import send_mail

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('users/', include(('users.urls', 'users'), namespace='users')),
    path('fields/', include(('fields.urls', 'fields'), namespace='fields')),
    path('activities/', include(('activities.urls', 'activities'), namespace='activities')),
    path('partner/', include(('partner.urls', 'partner'), namespace='partner')),
    path('activitycontrol/', include(('activitycontrol.urls', 'activitycontrol'), namespace='activitycontrol')),
    path('supplies/', include(('supplies.urls', 'supplies'), namespace='supplies')),
    path('home/', include(('home.urls', 'home'), namespace='home')),

    path('reset_password/', auth_views.PasswordResetView.as_view(
        template_name="reset_password.html",
        email_template_name="custom_password_reset_email.html"
    ), name="reset_password"),

    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="reset_password_sent.html"),
         name="password_reset_done"),

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="reset.html"),
         name="password_reset_confirm"),

    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="password_reset_complete.html"),
         name="password_reset_complete"),

]
from django.conf.urls import handler500
from django.conf.urls import handler404

handler500 = 'home.views.custom_500'

handler404 = 'home.views.custom_404'





