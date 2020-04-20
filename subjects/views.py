from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics

from .models import Subject
from .serializers import SubjectSerializer


class SubjectList(generics.ListCreateAPIView):
    """
    List all subjects, or create a new subject.
    列出所有学科，或者创建一个新的学科。
    """
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer


class SubjectDetail(APIView):
    """
        Get, update or delete a existed subject.
        获取、更新或删除一个现有的学科。
    """
    def get_object(self, subject_name):
        try:
            return Subject.objects.get(s_name=subject_name)
        except Subject.DoesNotExist:
            raise Http404

    def get(self, request, subject_name):
        subject = self.get_object(subject_name)
        serializer = SubjectSerializer(subject, context={'request': request})
        return Response(serializer.data)

    def put(self, request, subject_name):
        subject = self.get_object(subject_name)
        serializer = SubjectSerializer(subject, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, subject_name):
        subject = self.get_object(subject_name)
        subject.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
