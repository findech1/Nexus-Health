
# # analytics/views.py
# from rest_framework import generics
# from .models import AnalyticsRecord
# from .serializers import AnalyticsRecordSerializer

# class AnalyticsDashboardView(generics.ListCreateAPIView):
#     queryset = AnalyticsRecord.objects.all()
#     serializer_class = AnalyticsRecordSerializer

# class AnalyticsReportView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = AnalyticsRecord.objects.all()
#     serializer_class = AnalyticsRecordSerializer

# analytics/views.py
# analytics/views.py

from django.views.generic import TemplateView
from django.db.models import Sum
from .models import AnalyticsRecord

class AnalyticsDashboardView(TemplateView):
    template_name = 'analytics/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Count total patients
        context['total_patients'] = AnalyticsRecord.objects.filter(record_type='patient').count()

        # Count total appointments
        context['total_appointments'] = AnalyticsRecord.objects.filter(record_type='appointment').count()

        # Aggregate total revenue
        total_revenue = AnalyticsRecord.objects.filter(record_type='revenue').aggregate(Sum('data__amount'))
        context['total_revenue'] = total_revenue['data__amount__sum'] if total_revenue['data__amount__sum'] is not None else 0

        # Count pending bills
        context['pending_bills'] = AnalyticsRecord.objects.filter(record_type='bill', status='pending').count()

        return context

class AnalyticsReportView(TemplateView):
    template_name = 'analytics/report.html'
