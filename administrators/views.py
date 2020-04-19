from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics

from .models import Administrator, Permission
from .serializer import AdministratorSerializer, PermissionSerializer


class AdministratorList(generics.ListCreateAPIView):
    """
            List all administrators, or create a new administrator.
            列出所有用户，或者创建一个新用户。
    """
    queryset = Administrator.objects.all()
    serializer_class = AdministratorSerializer


class AdministratorDetail(APIView):
    """
        Get one administrator, or update or delete a existed administrator.
        获取、更新或删除一个现有的用户。
    """
    def get_object(self, admin_name):
        try:
            return Administrator.objects.get(admin_name=admin_name)
        except Administrator.DoesNotExist:
            raise Http404

    def get(self, request, admin_name):
        admin = self.get_object(admin_name)
        serializer = AdministratorSerializer(admin, context={'request': request})
        return Response(serializer.data)

    def put(self, request, admin_name):
        admin = self.get_object(admin_name)
        serializer = AdministratorSerializer(admin, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, admin_name):
        admin = self.get_object(admin_name)
        admin.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class PermissionList(generics.ListCreateAPIView):
    """
        List all permissions, or create a new permission.
        列出所有授权记录，或者创建一个新的授权记录。
    """
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer


class PermissionDetail(APIView):
    """
        Get, update or delete a existed permission.
        获取、更新或删除一个现有的授权记录。
    """

    def get_object(self, p_id):
        try:
            return Permission.objects.get(p_id=p_id)
        except Permission.DoesNotExist:
            raise Http404

    def get(self, request, permission_id):
        permission = self.get_object(permission_id)
        serializer = PermissionSerializer(permission, context={'request': request})
        return Response(serializer.data)

    def put(self, request, permission_id):
        permission = self.get_object(permission_id)
        serializer = PermissionSerializer(permission, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, permission_id):
        permission = self.get_object(permission_id)
        permission.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
