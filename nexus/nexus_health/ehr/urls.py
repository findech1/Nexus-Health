
# from django.urls import path
# from .views import EHRListView, EHRDetailView

# urlpatterns = [
#     path('', EHRListView.as_view(), name='ehr-list'),
#     path('<int:pk>/', EHRDetailView.as_view(), name='ehr-detail'),
# ]

# ehr/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.ehr_dashboard, name='ehr-dashboard'),
    path('health-records/', views.EHRListView.as_view(), name='ehr-list'),
    path('health-records/<int:pk>/', views.EHRDetailView.as_view(), name='ehr-detail'),
    path('products/', views.ProductListView.as_view(), name='product-list'),
    path('products/<int:pk>/', views.ProductDetailView.as_view(), name='product-detail'),
    path('inventory/', views.InventoryListView.as_view(), name='inventory-list'),
    path('inventory/<int:pk>/', views.InventoryDetailView.as_view(), name='inventory-detail'),
    path('sales/', views.SaleListView.as_view(), name='sale-list'),
    path('sales/<int:pk>/', views.SaleDetailView.as_view(), name='sale-detail'),
    path('billings/', views.BillingListView.as_view(), name='billing-list'),
    path('billings/<int:pk>/', views.BillingDetailView.as_view(), name='billing-detail'),
]
