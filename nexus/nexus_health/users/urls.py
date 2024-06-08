
# from django.urls import path
# from .views import CustomLoginView, doctor_homepage, patient_homepage, UserListView, UserDetailView

# urlpatterns = [
#     # HTML Views
#     path('login/', CustomLoginView.as_view(), name='account_login'),
#     path('doctor/homepage/', doctor_homepage, name='doctor-homepage'),
#     path('patient/homepage/', patient_homepage, name='patient-homepage'),

#     # API Views
#     path('api/users/', UserListView.as_view(), name='user-list'),
#     path('api/users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
# ]

from django.urls import path
from .views import (
    CustomLoginView,
    doctor_homepage,
    patient_homepage,
    UserListView,
    UserDetailView,
    AccountEmailVerificationSentView,
    CustomEmailVerificationSentView,
    profile_view,  # Add this import
)

urlpatterns = [
    # HTML Views
    path('login/', CustomLoginView.as_view(), name='account_login'),
    path('doctor/homepage/', doctor_homepage, name='doctor-homepage'),
    path('patient/homepage/', patient_homepage, name='patient-homepage'),
    path('auth/registration/account-email-verification-sent/', AccountEmailVerificationSentView.as_view(), name='account_email_verification_sent'),
    path('auth/registration/verification-sent/', CustomEmailVerificationSentView.as_view(), name='custom_email_verification_sent'),
    path('accounts/profile/', profile_view, name='profile'),  # Add this line

    # API Views
    path('api/users/', UserListView.as_view(), name='user-list'),
    path('api/users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
]
