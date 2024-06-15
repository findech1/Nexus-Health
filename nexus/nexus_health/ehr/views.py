
# from rest_framework import generics
# from .models import HealthRecord
# from .serializers import HealthRecordSerializer

# class EHRListView(generics.ListCreateAPIView):
#     queryset = HealthRecord.objects.all()
#     serializer_class = HealthRecordSerializer

# class EHRDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = HealthRecord.objects.all()
#     serializer_class = HealthRecordSerializer

# ehr/views.py

from django.shortcuts import render
from rest_framework import generics
from .models import HealthRecord, Product, Inventory, Sale, Billing
from .serializers import HealthRecordSerializer, ProductSerializer, InventorySerializer, SaleSerializer, BillingSerializer

def ehr_dashboard(request):
    # Example context data
    health_record_count = HealthRecord.objects.count()
    product_count = Product.objects.count()
    inventory_total = sum([entry.quantity for entry in Inventory.objects.all()])
    total_sales = Sale.objects.count()
    pending_billings = Billing.objects.filter(status='pending').count()

    context = {
        'health_record_count': health_record_count,
        'product_count': product_count,
        'inventory_total': inventory_total,
        'total_sales': total_sales,
        'pending_billings': pending_billings,
        # Add more context data as needed
    }
    return render(request, 'ehr/dashboard.html', context)

class EHRListView(generics.ListCreateAPIView):
    queryset = HealthRecord.objects.all()
    serializer_class = HealthRecordSerializer

class EHRDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = HealthRecord.objects.all()
    serializer_class = HealthRecordSerializer

class ProductListView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class InventoryListView(generics.ListCreateAPIView):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer

class InventoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer

class SaleListView(generics.ListCreateAPIView):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer

class SaleDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer

class BillingListView(generics.ListCreateAPIView):
    queryset = Billing.objects.all()
    serializer_class = BillingSerializer

class BillingDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Billing.objects.all()
    serializer_class = BillingSerializer
