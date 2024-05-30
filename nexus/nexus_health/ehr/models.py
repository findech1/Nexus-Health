from django.db import models
from users.models import CustomUser
from appointments.models import Appointment

class HealthRecord(models.Model):
    patient = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='health_records')
    appointment = models.OneToOneField(Appointment, on_delete=models.CASCADE)
    diagnosis = models.TextField()
    treatment_plan = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Health Record for {self.patient} on {self.created_at}"
