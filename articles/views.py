from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics

from .models import Article, ArticleHistory
from .serializer import ArticleSerializer, ArticleHistorySerializer


class ArticleList(generics.ListCreateAPIView):
    """
            List all articles, or create a new article.
            列出所有词条，或者创建一个新词条。
    """
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class ArticleDetail(APIView):
    """
        Get one article, or update or delete a existed article.
        获取、更新或删除一个现有的词条。
    """
    def get_object(self, subject_name, article_title):
        try:
            return Article.objects.get(a_subject__s_name=subject_name, a_title=article_title)
        except Article.DoesNotExist:
            raise Http404

    def get(self, request, subject_name, article_title):
        article = self.get_object(subject_name, article_title)
        serializer = ArticleSerializer(article, context={'request': request})
        return Response(serializer.data)

    def put(self, request, subject_name, article_title):
        article = self.get_object(subject_name, article_title)
        serializer = ArticleSerializer(article, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ArticleHistoryList(generics.ListCreateAPIView):
    """
        List all article's history, or create a new article's history.
        列出所有词条，或者创建一个新词条。
    """
    serializer_class = ArticleHistorySerializer

    def get_queryset(self):
        return ArticleHistory.objects.filter(
            ah_article__a_subject__s_name=self.kwargs['subject_name'],
            ah_article__a_title=self.kwargs['article_title']
        )
    # def get_objects(self, subject_name, article_title):
    #     try:
    #         return ArticleHistory.objects.filter(ah_article__a_subject__s_name=subject_name,
    #             ah_article__a_title=article_title)
    #     except ArticleHistory.DoesNotExist:
    #         raise Http404
    #
    # def get(self, request, subject_name, article_title):
    #     article_history = self.get_objects(subject_name, article_title)
    #     serializer = ArticleHistorySerializer(article_history, many=True, context={'request': request})
    #     return Response(serializer.data)

    # 更好的创建词条历史方式
    #     def post(self, request):
    #         serializer = ArticleHistorySerializer(data=request.data, context={'request': request})
    #         if serializer.is_valid():
    #             serializer.save()
    #             return Response(serializer.data, status=status.HTTP_201_CREATED)
    #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ArticleHistoryDetail(APIView):
    """
        Get one article's history.
        根据词条记录ID获取一个词条的记录。
    """
    def get_object(self, ah_id):
        try:
            return ArticleHistory.objects.get(ah_id=ah_id)
        except ArticleHistory.DoesNotExist:
            raise Http404

    def get(self, request, subject_name, article_title, ah_id):
        article_history = self.get_object(ah_id=ah_id)
        serializer = ArticleHistorySerializer(article_history, context={'request': request})
        return Response(serializer.data)
