"""
URL configuration for nexus_health project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
# from django.urls import path, include
# from django.shortcuts import render

# def home_view(request):
#     return render(request, 'home.html')

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('accounts/', include('allauth.urls')),
#     path('auth/', include('dj_rest_auth.urls')),
#     path('auth/registration/', include('dj_rest_auth.registration.urls')),
#     path('users/', include('users.urls')),
#     path('providers/', include('providers.urls')),
#     path('appointments/', include('appointments.urls')),
#     path('ehr/', include('ehr.urls')),
#     path('billing/', include('billing.urls')),
#     path('notifications/', include('notifications.urls')),
#     path('analytics/', include('analytics.urls')),
#     path('', home_view, name='home'),
# ]
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('auth/', include('dj_rest_auth.urls')),
    path('auth/registration/', include('dj_rest_auth.registration.urls')),
    path('users/', include('users.urls')),
    path('providers/', include('providers.urls')),
    path('appointments/', include('appointments.urls')),
    path('ehr/', include('ehr.urls')),
    path('billing/', include('billing.urls')),
    path('notifications/', include('notifications.urls')),
    path('analytics/', include('analytics.urls')),
    path('doctor/login/', TemplateView.as_view(template_name='users/doctor_login.html'), name='doctor-login'),
    path('patient/login/', TemplateView.as_view(template_name='users/patient_login.html'), name='patient-login'),
    path('', TemplateView.as_view(template_name='landing.html'), name='landing'),
]

