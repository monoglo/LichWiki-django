from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics

from .models import Model
from .serializers import ModelSerializer


class ModelList(generics.ListCreateAPIView):

    serializer_class = ModelSerializer

    def get_queryset(self):
        return Model.objects.filter(
            m_subject__s_name=self.kwargs['subject_name']
        )


class ModelDetail(APIView):
    def get_object(self, subject_name, model_name):
        try:
            return Model.objects.get(m_subject__s_name=subject_name, m_name=model_name)
        except Model.DoesNotExist:
            raise Http404

    def get(self, request, subject_name, model_name):
        model = self.get_object(subject_name, model_name)
        serializer = ModelSerializer(model, context={'request': request})
        return Response(serializer.data)

    def put(self, request, subject_name, model_name):
        model = self.get_object(subject_name, model_name)
        serializer = ModelSerializer(model, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, subject_name, model_name):
        model = self.get_object(subject_name, model_name)
        model.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
