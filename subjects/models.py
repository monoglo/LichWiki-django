from django.db import models

# Create your models here.


class Subject(models.Model):
    s_id = models.AutoField(primary_key=True)
    s_name = models.CharField(max_length=16, unique=True)

    def __str__(self):
        return self.s_name
