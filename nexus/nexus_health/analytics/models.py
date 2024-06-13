# from django.db import models
# from users.models import CustomUser
# from providers.models import Provider
# from appointments.models import Appointment

# class AnalyticsRecord(models.Model):
#     user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='analytics_records')
#     provider = models.ForeignKey(Provider, on_delete=models.CASCADE, related_name='analytics_records')
#     appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE, related_name='analytics_records')
#     data = models.JSONField()

#     def __str__(self):
#         return f"Analytics Record for {self.user} and {self.provider}"

from django.db import models
from users.models import CustomUser
from providers.models import Provider
from appointments.models import Appointment

class AnalyticsRecord(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='analytics_records')
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE, related_name='analytics_records')
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE, related_name='analytics_records')
    data = models.JSONField()
    record_type = models.CharField(max_length=50, default='appointment')  # Example default value 'appointment'
    status = models.CharField(max_length=50, null=True, blank=True)  # Example field for status

    def __str__(self):
        return f"Analytics Record for {self.user} and {self.provider}"
