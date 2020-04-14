from django.db import models
from django.contrib.auth.models import AbstractBaseUser
# Create your models here.


class User(models.Model):
    u_id = models.AutoField(primary_key=True)
    u_name = models.CharField(max_length=16, unique=True)
    u_email = models.CharField(max_length=24, unique=True)
    u_password = models.CharField(max_length=16)
    u_register_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.u_name
