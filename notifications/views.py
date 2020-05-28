from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics

from .models import Notification
from users.models import User


class SelectNotificationAmountByUserID(APIView):
    def get(self, request, user_name):
        user = User.objects.get(u_name=user_name)
        return Response(Notification.objects.filter(n_receiver_user=user.u_id, n_has_read=0).count())


class SelectNotificationListWithoutTextByUserID(APIView):
    pass


class SelectNotificationDetailByNotificationID(APIView):
    pass
