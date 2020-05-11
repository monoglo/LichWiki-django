from .models import Article, ArticleHistory
from rest_framework import serializers


class ArticleSerializer(serializers.HyperlinkedModelSerializer):
    subject_id = serializers.IntegerField(source='a_subject.s_id')
    subject_name = serializers.CharField(source='a_subject.s_name')
    author_id = serializers.IntegerField(source='a_author.u_id')
    author_name = serializers.CharField(source='a_author.u_name')

    class Meta:
        model = Article
        fields = ['a_id', 'subject_id', 'subject_name', 'author_id', 'author_name', 'a_title', 'a_text', 'a_length', 'a_create_time']

    def create(self, validated_data):
        return Article.objects.create(
            a_subject_id=validated_data.get('a_subject').get('s_id'),
            a_author_id=validated_data.get('a_author').get('u_id'),
            a_title=validated_data.get('a_title'),
            a_length=len(validated_data.get('a_title')),
            a_text=validated_data.get('a_text')
        )

    def update(self, instance, validated_data):
        print(validated_data)
        instance.subject_id = validated_data.get('a_subject').get('s_id')
        instance.author_id = validated_data.get('a_author').get('u_id')
        instance.a_title = validated_data.get('a_title')
        instance.a_length = len(validated_data.get('a_title'))
        instance.a_text = validated_data.get('a_text')
        instance.save()
        return instance


class ArticleHistorySerializer(serializers.HyperlinkedModelSerializer):
    article_id = serializers.IntegerField(source='ah_article.a_id')
    author_id = serializers.IntegerField(source='ah_author.u_id')
    author_name = serializers.CharField(source='ah_author.u_name')

    class Meta:
        model = ArticleHistory
        fields = ['ah_id', 'article_id', 'author_id', 'author_name', 'ah_summary', 'ah_title', 'ah_text', 'ah_length', 'ah_edit_time']

    def create(self, validated_data):
        return ArticleHistory.objects.create(
            ah_summary=validated_data.get('ah_summary'),
            ah_title=validated_data.get('ah_title'),
            ah_text=validated_data.get('ah_text'),
            ah_length=len(validated_data.get('ah_text')),
            ah_article_id=validated_data.get('ah_article').get('a_id'),
            ah_author_id=validated_data.get('ah_author').get('u_id')
        )
