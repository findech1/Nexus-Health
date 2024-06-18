
# from rest_framework import generics
# from .models import BillingRecord
# from .serializers import BillingRecordSerializer

# class BillingListView(generics.ListCreateAPIView):
#     queryset = BillingRecord.objects.all()
#     serializer_class = BillingRecordSerializer

# class BillingDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = BillingRecord.objects.all()
#     serializer_class = BillingRecordSerializer
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.db.models import Sum, Count
from .models import BillingRecord
from .forms import BillingRecordForm

def billing_dashboard(request):
    # Get the total number of billing records
    total_records = BillingRecord.objects.count()

    # Get the sum of all billing amounts
    total_amount = BillingRecord.objects.aggregate(total=Sum('amount'))['total']

    # Get the top 5 patients with the highest billing amounts
    top_patients = BillingRecord.objects.values('patient__username', 'patient__first_name', 'patient__last_name') \
                                          .annotate(total_amount=Sum('amount')) \
                                          .order_by('-total_amount')[:5]

    # Get the number of records for each status
    status_counts = BillingRecord.objects.values('status') \
                                          .annotate(count=Count('id'))

    context = {
        'total_records': total_records,
        'total_amount': total_amount,
        'top_patients': top_patients,
        'status_counts': status_counts,
    }

    return render(request, 'billing/dashboard.html', context)

def billing_list(request):
    billing_records = BillingRecord.objects.all()
    return render(request, 'billing/billing_list.html', {'billing_records': billing_records})

def billing_detail(request, pk):
    billing_record = get_object_or_404(BillingRecord, pk=pk)
    return render(request, 'billing/billing_detail.html', {'billing_record': billing_record})

def create_billing_record(request):
    if request.method == 'POST':
        form = BillingRecordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('billing-list')
    else:
        form = BillingRecordForm()
    return render(request, 'billing/billing_form.html', {'form': form})

def update_billing_record(request, pk):
    billing_record = get_object_or_404(BillingRecord, pk=pk)
    if request.method == 'POST':
        form = BillingRecordForm(request.POST, instance=billing_record)
        if form.is_valid():
            form.save()
            return redirect('billing-list')
    else:
        form = BillingRecordForm(instance=billing_record)
    return render(request, 'billing/billing_form.html', {'form': form})

def delete_billing_record(request, pk):
    billing_record = get_object_or_404(BillingRecord, pk=pk)
    if request.method == 'POST':
        billing_record.delete()
        return redirect('billing-list')
    return render(request, 'billing/billing_confirm_delete.html', {'billing_record': billing_record})