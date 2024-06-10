
from django.urls import path
from .views import AnalyticsDashboardView, AnalyticsReportView

urlpatterns = [
    path('dashboard/', AnalyticsDashboardView.as_view(), name='analytics-dashboard'),
    path('report/', AnalyticsReportView.as_view(), name='analytics-report'),
]
