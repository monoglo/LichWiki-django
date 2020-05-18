from django.db import models
from users.models import User


class Comment(models.Model):
    c_id = models.IntegerField(primary_key=True)
    c_url = models.CharField(max_length=256)
    c_text = models.TextField(max_length=256)
    c_user = models.ForeignKey(User, on_delete=models.CASCADE)
    c_father_comment_id = models.IntegerField(null=True)
    c_create_time = models.DateTimeField(auto_now_add=True)
