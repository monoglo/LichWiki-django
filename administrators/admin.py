from django.contrib import admin
from .models import Administrator, Permission
# Register your models here.

admin.site.register(Administrator)
admin.site.register(Permission)

