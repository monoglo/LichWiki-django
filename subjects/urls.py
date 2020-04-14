from django.urls import include, path
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

app_name = 'subjects'
urlpatterns = [
    path('api/subjects/', views.SubjectList.as_view()),
    path('api/subject/<str:subject_name>', views.SubjectDetail.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)
