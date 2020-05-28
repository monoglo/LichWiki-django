from django.db import models
from users.models import User


class Notification(models.Model):
    n_id = models.IntegerField(primary_key=True)
    n_title = models.CharField(max_length=128)
    n_text = models.CharField(max_length=256)
    n_receiver_user = models.ForeignKey(User, related_name='receiver_user', on_delete=models.CASCADE)
    n_sender_user = models.ForeignKey(User, related_name='sender_user', default=0, on_delete=models.CASCADE)
    n_has_read = models.BooleanField(default=0)
    n_create_time = models.DateTimeField(auto_now_add=True)
