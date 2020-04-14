from django.db import models
from users.models import User
# Create your models here.


class Model(models.Model):
    m_id = models.AutoField(primary_key=True)
    m_name = models.CharField(max_length=128)
    m_text = models.TextField()
    m_user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    m_create_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.m_name
