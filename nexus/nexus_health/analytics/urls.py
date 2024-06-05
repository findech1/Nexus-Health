# from django.urls import path
# from .views import AnalyticsRecordListView, AnalyticsRecordDetailView

# urlpatterns = [
#     path('', AnalyticsRecordListView.as_view(), name='analytics-record-list'),
#     path('<int:pk>/', AnalyticsRecordDetailView.as_view(), name='analytics-record-detail'),
# ]
from django.urls import path
from .views import AnalyticsDashboardView, AnalyticsReportView

urlpatterns = [
    path('dashboard/', AnalyticsDashboardView.as_view(), name='analytics-dashboard'),
    path('report/', AnalyticsReportView.as_view(), name='analytics-report'),
]
