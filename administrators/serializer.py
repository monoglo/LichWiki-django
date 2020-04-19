from .models import Administrator, Permission
from rest_framework import serializers


class AdministratorSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Administrator
        fields = ['admin_id', 'admin_name', 'admin_email', 'admin_password']


class PermissionSerializer(serializers.HyperlinkedModelSerializer):
    admin_id = serializers.IntegerField(source='p_admin.admin_id')
    # admin_name = serializers.CharField(source='p_admin.admin_name')
    user_id = serializers.IntegerField(source='p_user.u_id')
    # user_name = serializers.CharField(source='p_user.u_name')
    p_permission_node = serializers.CharField()

    class Meta:
        model = Permission
        fields = ['p_id', 'admin_id', 'user_id', 'p_permission_node', 'p_time']

    def create(self, validated_data):
        return Permission.objects.create(
            p_admin_id=validated_data.get('p_admin.admin_id'),
            p_user_id=validated_data.get('p_user.u_id'),
            p_permission_node=validated_data.get('p_permission_node')
        )
