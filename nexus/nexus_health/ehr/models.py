# from django.db import models
# from users.models import CustomUser
# from appointments.models import Appointment

# class HealthRecord(models.Model):
#     patient = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='health_records')
#     appointment = models.OneToOneField(Appointment, on_delete=models.CASCADE)
#     diagnosis = models.TextField()
#     treatment_plan = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"Health Record for {self.patient} on {self.created_at}"

# ehr/models.py

from django.db import models
from users.models import CustomUser
from appointments.models import Appointment
from providers.models import Provider

class HealthRecord(models.Model):
    patient = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='health_records')
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE, related_name='health_records')
    diagnosis = models.TextField()
    treatment_plan = models.TextField()

    def __str__(self):
        return f"Health Record for {self.patient} on {self.appointment}"

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()

    def __str__(self):
        return self.name

class Inventory(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='inventory_entries')
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.quantity} of {self.product.name}"

class Sale(models.Model):
    patient = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='sales')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='sales')
    quantity = models.PositiveIntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    sale_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Sale of {self.quantity} {self.product.name} to {self.patient}"

class Billing(models.Model):
    patient = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='billings')
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE, related_name='billings')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=[('pending', 'Pending'), ('paid', 'Paid')])

    def __str__(self):
        return f"Billing for {self.patient} - {self.status}"
