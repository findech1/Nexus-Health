# # billing/forms.py
# from django import forms
# from .models import BillingRecord

# class BillingRecordForm(forms.ModelForm):
#     class Meta:
#         model = BillingRecord
#         fields = ['patient', 'appointment', 'amount', 'status']
# billing/forms.py
from django import forms
from .models import BillingRecord

class BillingRecordForm(forms.ModelForm):
    class Meta:
        model = BillingRecord
        fields = ['patient', 'appointment', 'amount', 'status']