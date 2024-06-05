# from django.urls import path
# from .views import ProviderListView, ProviderDetailView, SpecialtyListView, SpecialtyDetailView

# urlpatterns = [
#     path('providers/', ProviderListView.as_view(), name='provider-list'),
#     path('providers/<int:pk>/', ProviderDetailView.as_view(), name='provider-detail'),
#     path('specialties/', SpecialtyListView.as_view(), name='specialty-list'),
#     path('specialties/<int:pk>/', SpecialtyDetailView.as_view(), name='specialty-detail'),
# ]
from django.urls import path
from .views import ProviderListView, ProviderDetailView

urlpatterns = [
    path('', ProviderListView.as_view(), name='provider-list'),
    path('<int:pk>/', ProviderDetailView.as_view(), name='provider-detail'),
]
