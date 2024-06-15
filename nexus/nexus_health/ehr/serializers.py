# from rest_framework import serializers
# from .models import HealthRecord

# class HealthRecordSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = HealthRecord
#         fields = ['id', 'patient', 'appointment', 'diagnosis', 'treatment_plan', 'created_at']

# ehr/serializers.py

from rest_framework import serializers
from .models import HealthRecord, Product, Inventory, Sale, Billing

class HealthRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = HealthRecord
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = '__all__'

class SaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sale
        fields = '__all__'

class BillingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Billing
        fields = '__all__'
