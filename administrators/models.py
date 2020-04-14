from django.db import models
from users.models import User

# Create your models here.


class Administrator(models.Model):
    admin_id = models.AutoField(primary_key=True)
    admin_name = models.CharField(max_length=16, unique=True)
    admin_email = models.CharField(max_length=24)
    admin_password = models.CharField(max_length=16)

    def __str__(self):
        return self.admin_name


class Permission(models.Model):
    p_id = models.AutoField(primary_key=True)
    p_admin = models.ForeignKey(Administrator, null=True, on_delete=models.SET_NULL)
    p_user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    p_permission_node = models.CharField(max_length=128)
    p_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.p_permission_node
