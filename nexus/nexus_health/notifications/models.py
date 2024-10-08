# from django.db import models
# from users.models import CustomUser

# class Notification(models.Model):
#     user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='notifications')
#     message = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     read = models.BooleanField(default=False)

#     def __str__(self):
#         return f"Notification for {self.user} - {'Read' if self.read else 'Unread'}"
# models.py

from django.db import models
from users.models import CustomUser

class Notification(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='notifications')
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)

    def __str__(self):
        return f"Notification for {self.user} - {'Read' if self.read else 'Unread'}"
