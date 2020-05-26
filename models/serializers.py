from .models import Model
from rest_framework import serializers


class ModelSerializer(serializers.HyperlinkedModelSerializer):
    subject_id = serializers.IntegerField(source='m_subject.s_id')
    author_id = serializers.IntegerField(source='m_author.u_id')

    class Meta:
        model = Model
        fields = ['m_id', 'm_name', 'm_text', 'subject_id', 'author_id', 'm_create_time']

    def create(self, validated_data):
        if Model.objects.filter(m_name=validated_data.get('m_name'),
                                m_subject_id=validated_data.get('m_subject').get('s_id')):
            raise Model.MultipleObjectsReturned
        else:
            model = Model.objects.create(
                m_subject_id=validated_data.get('m_subject').get('s_id'),
                m_author_id=validated_data.get('m_author').get('u_id'),
                m_name=validated_data.get('m_name'),
                m_text=validated_data.get('m_text'),
            )
            return model

    def update(self, instance, validated_data):
        instance.subject_id = validated_data.get('m_subject').get('s_id')
        instance.author_id = validated_data.get('m_author').get('u_id')
        instance.m_name = validated_data.get('m_name')
        instance.m_text = validated_data.get('m_text')
        instance.save()
        return instance
