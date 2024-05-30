from django.urls import path
from .views import HealthRecordListView, HealthRecordDetailView

urlpatterns = [
    path('', HealthRecordListView.as_view(), name='health-record-list'),
    path('<int:pk>/', HealthRecordDetailView.as_view(), name='health-record-detail'),
]
