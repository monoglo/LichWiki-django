from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics

from .models import Notification
from users.models import User
from .serializers import NotificationSerializer


class SelectUnreadNotificationAmountByUserID(APIView):
    def get(self, request, user_name):
        return Response(Notification.objects.filter(n_receiver_user__u_name=user_name, n_has_read=0).count())


class SelectAllNotificationWithoutTextByUserName(APIView):
    def get(self, request, user_name):
        notification = Notification.objects.filter(n_receiver_user__u_name=user_name)
        notification_serializer = NotificationSerializer(notification, many=True, context={'request': request})
        if notification:
            response_data = notification_serializer.data
            for item in response_data:
                item.pop('n_has_read')
                item.pop('n_text')
            return Response(response_data)
        else:
            return Response(status.HTTP_404_NOT_FOUND)


class SelectNotificationDetailByNotificationID(APIView):
    def get(self, request, n_id):
        notification = Notification.objects.get(n_id=n_id)
        notification_serializer = NotificationSerializer(notification, context={'request': request})
        if notification:
            notification.n_has_read = 1
            notification.save()
            return Response(notification_serializer.data)
        else:
            return Response(status.HTTP_404_NOT_FOUND)


class CreateNotification(generics.ListCreateAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer

