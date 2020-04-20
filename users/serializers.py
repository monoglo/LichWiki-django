from .models import User
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ['u_id', 'u_name', 'u_email', 'u_password', 'u_register_time']
