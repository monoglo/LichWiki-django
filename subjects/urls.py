from django.urls import include, path
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

app_name = 'subjects'
urlpatterns = [
    path('subjects/', views.SubjectList.as_view()),
    path('subjects/<str:subject_name>', views.SubjectDetail.as_view())
]
