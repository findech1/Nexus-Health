from rest_framework import serializers
from .models import HealthRecord

class HealthRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = HealthRecord
        fields = ['id', 'patient', 'appointment', 'diagnosis', 'treatment_plan', 'created_at']
