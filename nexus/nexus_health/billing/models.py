from django.db import models
from users.models import CustomUser
from appointments.models import Appointment

class BillingRecord(models.Model):
    patient = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='billing_records')
    appointment = models.OneToOneField(Appointment, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=[('paid', 'Paid'), ('pending', 'Pending'), ('invoiced', 'invoiced'), ('due', 'due')])

    def __str__(self):
        return f"Billing Record for {self.patient} - {self.status}"
