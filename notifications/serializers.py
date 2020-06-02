from rest_framework import serializers
from .models import Notification


class NotificationSerializer(serializers.HyperlinkedModelSerializer):
    n_receiver_user_id = serializers.IntegerField(source='n_receiver_user.u_id')
    n_sender_user_id = serializers.IntegerField(source='n_sender_user.u_id')
    n_sender_user_name = serializers.CharField(source='n_sender_user.u_name')

    class Meta:
        model = Notification
        fields = ['n_id', 'n_title', 'n_text', 'n_receiver_user_id', 'n_sender_user_id', 'n_sender_user_name',
                  'n_has_read', 'n_create_time']

    def create(self, validated_data):
        return Notification.objects.create(
            n_title=validated_data.get('n_title'),
            n_text=validated_data.get('n_text'),
            n_receiver_user_id=validated_data.get('n_receiver_user').get('u_id'),
            n_sender_user_id=validated_data.get('n_sender_user').get('u_id'),
        )


class CreateNotificationSerializer(serializers.HyperlinkedModelSerializer):
    n_receiver_user_id = serializers.IntegerField(source='n_receiver_user.u_id')
    n_sender_user_id = serializers.IntegerField(source='n_sender_user.u_id')

    class Meta:
        model = Notification
        fields = ['n_title', 'n_text', 'n_receiver_user_id', 'n_sender_user_id']

    def create(self, validated_data):
        return Notification.objects.create(
            n_title=validated_data.get('n_title'),
            n_text=validated_data.get('n_text'),
            n_receiver_user_id=validated_data.get('n_receiver_user').get('u_id'),
            n_sender_user_id=validated_data.get('n_sender_user').get('u_id'),
        )