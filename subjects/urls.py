from django.urls import include, path
from rest_framework import routers
from subjects import views

urlpatterns = [
    path('subjects/', views.subject_list),
    path('subjects/<str:subject_name>', views.subject_detail)
]
