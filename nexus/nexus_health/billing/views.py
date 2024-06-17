
# from rest_framework import generics
# from .models import BillingRecord
# from .serializers import BillingRecordSerializer

# class BillingListView(generics.ListCreateAPIView):
#     queryset = BillingRecord.objects.all()
#     serializer_class = BillingRecordSerializer

# class BillingDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = BillingRecord.objects.all()
#     serializer_class = BillingRecordSerializer
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .models import BillingRecord
from .forms import BillingRecordForm



def billing_list(request):
    bills = BillingRecord.objects.all()
    return render(request, 'billing/billing_list.html', {'bills': bills})

def billing_detail(request, pk):
    bill = BillingRecord.objects.get(pk=pk)
    return render(request, 'billing/billing_detail.html', {'bill': bill})

def create_billing_record(request):
    if request.method == 'POST':
        form = BillingRecordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy('billing_list'))
    else:
        form = BillingRecordForm()
    return render(request, 'billing/billing_form.html', {'form': form})

def update_billing_record(request, pk):
    bill = BillingRecord.objects.get(pk=pk)
    if request.method == 'POST':
        form = BillingRecordForm(request.POST, instance=bill)
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy('billing_list'))
    else:
        form = BillingRecordForm(instance=bill)
    return render(request, 'billing/billing_form.html', {'form': form})

def delete_billing_record(request, pk):
    bill = BillingRecord.objects.get(pk=pk)
    bill.delete()
    return redirect(reverse_lazy('billing_list'))
def billing_list(request):
    billing_records = BillingRecord.objects.all()
    return render(request, 'billing/billing_list.html', {'billing_records': billing_records})