from rest_framework import serializers
from .models import Notification


class NotificationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Notification
        fields = ['n_id', 'n_title', 'n_text', 'n_receiver_user', 'n_sender_user', 'n_has_read', 'n_create_time']
