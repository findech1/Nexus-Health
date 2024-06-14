# from django.db import models
# from users.models import CustomUser
# from providers.models import Provider

# class Appointment(models.Model):
#     patient = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='appointments')
#     provider = models.ForeignKey(Provider, on_delete=models.CASCADE, related_name='appointments')
#     date_time = models.DateTimeField()
#     reason = models.TextField()

#     def __str__(self):
#         return f"{self.patient} - {self.provider} on {self.date_time}"

from django.db import models

class Appointment(models.Model):
    patient = models.CharField(max_length=100)
    provider = models.CharField(max_length=100)
    date_time = models.DateTimeField()
    reason = models.TextField()

    def __str__(self):
        return f"Appointment with {self.patient} by {self.provider} on {self.date_time}"
