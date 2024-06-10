
from django.urls import path
from .views import EHRListView, EHRDetailView

urlpatterns = [
    path('', EHRListView.as_view(), name='ehr-list'),
    path('<int:pk>/', EHRDetailView.as_view(), name='ehr-detail'),
]
