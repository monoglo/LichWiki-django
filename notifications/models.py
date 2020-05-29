from django.db import models
from users.models import User


class Notification(models.Model):
    n_id = models.AutoField(primary_key=True)
    n_title = models.CharField(max_length=128)
    n_text = models.CharField(max_length=256)
    n_create_time = models.DateTimeField(auto_now_add=True)
    n_receiver_user = models.ForeignKey(User, related_name='n_receiver_user', on_delete=models.CASCADE)
    n_sender_user = models.ForeignKey(User, related_name='n_sender_user', null=True, on_delete=models.SET_NULL)
    n_has_read = models.BooleanField(default=0)
