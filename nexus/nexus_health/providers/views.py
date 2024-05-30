from rest_framework import generics
from .models import Provider, Specialty
from .serializers import ProviderSerializer, SpecialtySerializer

class ProviderListView(generics.ListCreateAPIView):
    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer

class ProviderDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer

class SpecialtyListView(generics.ListCreateAPIView):
    queryset = Specialty.objects.all()
    serializer_class = SpecialtySerializer

class SpecialtyDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Specialty.objects.all()
    serializer_class = SpecialtySerializer
