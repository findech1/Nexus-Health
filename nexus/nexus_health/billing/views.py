# from rest_framework import generics
# from .models import BillingRecord
# from .serializers import BillingRecordSerializer

# class BillingRecordListView(generics.ListCreateAPIView):
#     queryset = BillingRecord.objects.all()
#     serializer_class = BillingRecordSerializer

# class BillingRecordDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = BillingRecord.objects.all()
#     serializer_class = BillingRecordSerializer
# billing/views.py
from rest_framework import generics
from .models import BillingRecord
from .serializers import BillingRecordSerializer

class BillingListView(generics.ListCreateAPIView):
    queryset = BillingRecord.objects.all()
    serializer_class = BillingRecordSerializer

class BillingDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BillingRecord.objects.all()
    serializer_class = BillingRecordSerializer
