# from django.urls import path
# from .views import BillingRecordListView, BillingRecordDetailView

# urlpatterns = [
#     path('', BillingRecordListView.as_view(), name='billing-record-list'),
#     path('<int:pk>/', BillingRecordDetailView.as_view(), name='billing-record-detail'),
# ]
from django.urls import path
from .views import BillingListView, BillingDetailView

urlpatterns = [
    path('', BillingListView.as_view(), name='billing-list'),
    path('<int:pk>/', BillingDetailView.as_view(), name='billing-detail'),
]
