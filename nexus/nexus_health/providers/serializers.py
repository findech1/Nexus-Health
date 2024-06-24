from rest_framework import serializers
from .models import Provider, Specialty

class SpecialtySerializer(serializers.ModelSerializer):
    class Meta:
        model = Specialty
        fields = ['id', 'name']

class ProviderSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    specialty = serializers.PrimaryKeyRelatedField(queryset=Specialty.objects.all())

    class Meta:
        model = Provider
        fields = ['id', 'user', 'specialty', 'availability']
