from article_templates.models import ArticleTemplate
from rest_framework import serializers


class GetModelSerializer(serializers.HyperlinkedModelSerializer):
    subject_id = serializers.IntegerField(source='m_subject.s_id')
    author_id = serializers.IntegerField(source='m_author.u_id')

    class Meta:
        model = ArticleTemplate
        fields = ['m_id', 'm_name', 'm_text', 'subject_id', 'author_id', 'm_create_time']

    def create(self, validated_data):
        if ArticleTemplate.objects.filter(m_name=validated_data.get('m_name'),
                                          m_subject_id=validated_data.get('m_subject').get('s_id')):
            raise ArticleTemplate.MultipleObjectsReturned
        else:
            model = ArticleTemplate.objects.create(
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


class PostModelSerializer(GetModelSerializer):
    author_name = serializers.CharField(source='m_author.u_name')

    class Meta:
        model = ArticleTemplate
        fields = ['m_id', 'm_name', 'm_text', 'subject_id', 'author_id', 'author_name', 'm_create_time']

