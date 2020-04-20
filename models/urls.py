from django.urls import path

from . import views

app_name = 'models'
urlpatterns = [
    path('models/<str:subject_name>', views.ModelList.as_view()),
    path('models/<str:subject_name>/<str:model_name>', views.ModelDetail.as_view())
]