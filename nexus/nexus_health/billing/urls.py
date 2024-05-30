from django.urls import path
from .views import BillingRecordListView, BillingRecordDetailView

urlpatterns = [
    path('', BillingRecordListView.as_view(), name='billing-record-list'),
    path('<int:pk>/', BillingRecordDetailView.as_view(), name='billing-record-detail'),
]
