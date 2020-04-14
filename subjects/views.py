from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.parsers import JSONParser

from .models import Subject
from .serializer import SubjectSerializer
# Create your views here.


class SubjectViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows subjects to be viewed or edited.
    """
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    permission_classes = [permissions.IsAuthenticated]


@csrf_exempt
def subject_list(request, pk):
    """
    List all subjects, or create a new subject.
    :param request:
    :param pk:
    :return:
    """
    try:
        subject = Subject.objects.get(pk=pk)
    except Subject.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = SubjectSerializer(subject)
        return JsonResponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = SubjectSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def subject_detail(request, subject_name):
    try:
        subject = Subject.objects.get(s_name=subject_name)
    except Subject.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = SubjectSerializer(subject, context={'request': request})
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = SubjectSerializer(subject, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        subject.delete()
        return HttpResponse(status=204)

