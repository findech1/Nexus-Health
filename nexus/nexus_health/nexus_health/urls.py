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
# # nexus_health/urls.py

# nexus_health/urls.py

from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from users.views import profile_view  # Import the profile_view function
from allauth.account.views import LoginView, SignupView  # Import the LoginView and SignupView

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
    path('doctor/login/', LoginView.as_view(), name='doctor-login'),  # Use LoginView for doctor login
    path('patient/login/', LoginView.as_view(), name='patient-login'),  # Use LoginView for patient login
    path('accounts/signup/', SignupView.as_view(), name='account_signup'),  # Use SignupView for signup
    path('accounts/profile/', profile_view, name='profile'),
    path('', TemplateView.as_view(template_name='landing.html'), name='landing'),
]
    