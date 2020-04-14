from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import User
from .serializer import UserSerializer


class UserList(APIView):

    def get(self, request, format=None):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True, context={'request': request})
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDetail(APIView):

    def get_object(self, user_name):
        try:
            return User.objects.get(u_name=user_name)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, user_name, format=None):
        user = self.get_object(user_name)
        serializer = UserSerializer(user, context={'request': request})
        return Response(serializer.data)

    def put(self, request, user_name, format=None):
        user = self.get_object(user_name)
        serializer = UserSerializer(user, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, user_name, format=None):
        user = self.get_object(user_name)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

'''
class UserLogin(APIView):

    def post(self, request):

'''
