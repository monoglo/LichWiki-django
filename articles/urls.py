from django.urls import path

from . import views

app_name = 'articles'
urlpatterns = [
    path('articles/<str:subject_name>', views.ArticleList.as_view()),
    path('articles/<str:subject_name>/<str:article_title>', views.ArticleDetail.as_view()),
    path('articles/<str:subject_name>/<str:article_title>/history', views.ArticleHistoryList.as_view()),
    path('articles/<str:subject_name>/<str:article_title>/history/<int:ah_id>', views.ArticleHistoryDetail.as_view())
]
