from rest_framework import generics
from .models import AnalyticsRecord
from .serializers import AnalyticsRecordSerializer

class AnalyticsRecordListView(generics.ListCreateAPIView):
    queryset = AnalyticsRecord.objects.all()
    serializer_class = AnalyticsRecordSerializer

class AnalyticsRecordDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = AnalyticsRecord.objects.all()
    serializer_class = AnalyticsRecordSerializer
