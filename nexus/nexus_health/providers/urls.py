
# # ]
# from django.urls import path
# from .views import ProviderListView, ProviderDetailView

# urlpatterns = [
#     path('', ProviderListView.as_view(), name='provider-list'),
#     path('<int:pk>/', ProviderDetailView.as_view(), name='provider-detail'),
# ]

# urls.py
from django.urls import path
from .views import (
    DashboardView, ProviderListView, ProviderDetailView,
    ProviderCreateView, ProviderUpdateView, ProviderDeleteView,
    SpecialtyListView, SpecialtyDetailView, SpecialtyCreateView,
    SpecialtyUpdateView, SpecialtyDeleteView
)

urlpatterns = [
    path('', DashboardView.as_view(), name='dashboard'),
    path('providers/', ProviderListView.as_view(), name='provider-list'),
    path('providers/create/', ProviderCreateView.as_view(), name='provider-create'),
    path('providers/<int:pk>/', ProviderDetailView.as_view(), name='provider-detail'),
    path('providers/<int:pk>/update/', ProviderUpdateView.as_view(), name='provider-update'),
    path('providers/<int:pk>/delete/', ProviderDeleteView.as_view(), name='provider-delete'),
    path('specialties/', SpecialtyListView.as_view(), name='specialty-list'),
    path('specialties/create/', SpecialtyCreateView.as_view(), name='specialty-create'),
    path('specialties/<int:pk>/', SpecialtyDetailView.as_view(), name='specialty-detail'),
    path('specialties/<int:pk>/update/', SpecialtyUpdateView.as_view(), name='specialty-update'),
    path('specialties/<int:pk>/delete/', SpecialtyDeleteView.as_view(), name='specialty-delete'),
]
