from .models import Comment
from rest_framework import serializers


class CommentGetSerializer(serializers.HyperlinkedModelSerializer):
    c_user_id = serializers.IntegerField(source='c_user.u_id')
    c_user_name = serializers.CharField(source='c_user.u_name')

    class Meta:
        model = Comment
        fields = ['c_id', 'c_url', 'c_text', 'c_user_id', 'c_user_name', 'c_father_comment_id', 'c_create_time']


class CommentCreateSerializer(serializers.HyperlinkedModelSerializer):
    c_user_id = serializers.IntegerField(source='c_user.u_id')

    def create(self, validated_data):
        return Comment.objects.create(
            c_url=validated_data.get('c_url'),
            c_text=validated_data.get('c_text'),
            c_user_id=validated_data.get('c_user').get('u_id'),
            c_father_comment_id=validated_data.get('c_father_comment_id')
        )

    class Meta:
        model = Comment
        fields = ['c_url', 'c_text', 'c_user_id', 'c_father_comment_id']
