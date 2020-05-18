from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics

from .models import Comment
from .serializers import CommentGetSerializer, CommentCreateSerializer


class SelectOrCreateCommentsByURL(APIView):
    """
    Response comments by get URL or Create a new comment by post info.
    获取某一URL下所有评论或创建一条新的评论。
    """
    def get_objects(self, url):
        try:
            return Comment.objects.filter(c_url=url)
        except Comment.DoesNotExist:
            raise Http404

    def get(self, request):
        print(request.query_params['c_url'])
        comments = self.get_objects(request.query_params['c_url'])
        comments_serializer = CommentGetSerializer(comments, context={'request': request}, many=True)
        return Response(comments_serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        comment_serializer = CommentCreateSerializer(data=request.data, context={'request': request})
        if comment_serializer.is_valid():
            comment_serializer.save()
            return Response(comment_serializer.data)
        else:
            return Response(comment_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
