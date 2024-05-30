from django.db import models
from users.models import CustomUser

class Specialty(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Provider(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    specialty = models.ForeignKey(Specialty, on_delete=models.SET_NULL, null=True)
    availability = models.TextField()  # JSON or text representation of availability

    def __str__(self):
        return self.user.get_full_name()
