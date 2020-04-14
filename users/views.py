from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics

from .models import User
from .serializer import UserSerializer


class UserList(generics.ListCreateAPIView):
    """
        List all users, or create a new user.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(APIView):
    """
        Get one user, or update or delete a existed user.
    """
    def get_object(self, user_name):
        try:
            return User.objects.get(u_name=user_name)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, user_name):
        user = self.get_object(user_name)
        serializer = UserSerializer(user, context={'request': request})
        return Response(serializer.data)

    def put(self, request, user_name):
        user = self.get_object(user_name)
        serializer = UserSerializer(user, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, user_name):
        user = self.get_object(user_name)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

'''
class UserLogin(APIView):

    def post(self, request):

'''
