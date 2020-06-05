from django.urls import path

from article_templates import views

app_name = 'article_templates'
urlpatterns = [
    path('models/<str:subject_name>', views.ModelList.as_view()),
    path('models/<str:subject_name>/<str:model_name>', views.ModelDetail.as_view())
]