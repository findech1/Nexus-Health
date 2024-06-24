# from rest_framework import generics
# from .models import Provider, Specialty
# from .serializers import ProviderSerializer, SpecialtySerializer

# class ProviderListView(generics.ListCreateAPIView):
#     queryset = Provider.objects.all()
#     serializer_class = ProviderSerializer

# class ProviderDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Provider.objects.all()
#     serializer_class = ProviderSerializer

# class SpecialtyListView(generics.ListCreateAPIView):
#     queryset = Specialty.objects.all()
#     serializer_class = SpecialtySerializer

# class SpecialtyDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Specialty.objects.all()
#     serializer_class = SpecialtySerializer

# views.py
# views.py
from django.shortcuts import render
from rest_framework import generics
from .models import Provider, Specialty
from .serializers import ProviderSerializer, SpecialtySerializer

class DashboardView(generics.GenericAPIView):
    def get(self, request):
        return render(request, 'providers/dashboard.html')

class ProviderListView(generics.ListCreateAPIView):
    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer
    template_name = 'provider_list.html'

class ProviderDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer
    template_name = 'provider_detail.html'

class ProviderCreateView(generics.CreateAPIView):
    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer
    template_name = 'provider_form.html'

class ProviderUpdateView(generics.UpdateAPIView):
    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer
    template_name = 'provider_form.html'

class ProviderDeleteView(generics.DestroyAPIView):
    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer
    template_name = 'provider_confirm_delete.html'

class SpecialtyListView(generics.ListCreateAPIView):
    queryset = Specialty.objects.all()
    serializer_class = SpecialtySerializer
    template_name = 'specialty_list.html'

class SpecialtyDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Specialty.objects.all()
    serializer_class = SpecialtySerializer
    template_name = 'specialty_detail.html'

class SpecialtyCreateView(generics.CreateAPIView):
    queryset = Specialty.objects.all()
    serializer_class = SpecialtySerializer
    template_name = 'specialty_form.html'

class SpecialtyUpdateView(generics.UpdateAPIView):
    queryset = Specialty.objects.all()
    serializer_class = SpecialtySerializer
    template_name = 'specialty_form.html'

class SpecialtyDeleteView(generics.DestroyAPIView):
    queryset = Specialty.objects.all()
    serializer_class = SpecialtySerializer
    template_name = 'specialty_confirm_delete.html'
