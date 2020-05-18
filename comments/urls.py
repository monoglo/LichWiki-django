from django.urls import path

from . import views


app_name = 'comments'
urlpatterns = [
    path('comments/', views.SelectOrCreateCommentsByURL.as_view())
]
