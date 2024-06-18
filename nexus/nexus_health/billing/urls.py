
# from django.urls import path
# from .views import BillingListView, BillingDetailView

# urlpatterns = [
#     path('', BillingListView.as_view(), name='billing-list'),
#     path('<int:pk>/', BillingDetailView.as_view(), name='billing-detail'),
# ]
from django.urls import path
from . import views

# app_name = 'billing'

urlpatterns = [
    path('', views.billing_dashboard, name='billing-dashboard'),
    path('billng', views.billing_list, name='billing-list'),
    path('billing/<int:pk>/', views.billing_detail, name='billing-detail'),
    path('billing/create/', views.create_billing_record, name='create-billing-record'),
    path('billing/<int:pk>/update/', views.update_billing_record, name='update-billing-record'),
    path('billing/<int:pk>/delete/', views.delete_billing_record, name='delete-billing-record'),
]