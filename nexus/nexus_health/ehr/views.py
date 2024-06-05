# from rest_framework import generics
# from .models import HealthRecord
# from .serializers import HealthRecordSerializer

# class HealthRecordListView(generics.ListCreateAPIView):
#     queryset = HealthRecord.objects.all()
#     serializer_class = HealthRecordSerializer

# class HealthRecordDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = HealthRecord.objects.all()
#     serializer_class = HealthRecordSerializer
# views.py in ehr app
from rest_framework import generics
from .models import HealthRecord
from .serializers import HealthRecordSerializer

class EHRListView(generics.ListCreateAPIView):
    queryset = HealthRecord.objects.all()
    serializer_class = HealthRecordSerializer

class EHRDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = HealthRecord.objects.all()
    serializer_class = HealthRecordSerializer
