from django.urls import path
from .views import AnalyticsRecordListView, AnalyticsRecordDetailView

urlpatterns = [
    path('', AnalyticsRecordListView.as_view(), name='analytics-record-list'),
    path('<int:pk>/', AnalyticsRecordDetailView.as_view(), name='analytics-record-detail'),
]
