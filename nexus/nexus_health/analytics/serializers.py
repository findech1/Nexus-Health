from rest_framework import serializers
from .models import AnalyticsRecord

class AnalyticsRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnalyticsRecord
        fields = ['id', 'user', 'provider', 'appointment', 'data']
