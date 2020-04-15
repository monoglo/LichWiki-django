from django.urls import path

from . import views

app_name = 'administrators'
urlpatterns = [
    path('admins/', views.AdministratorList.as_view()),
    path('admins/<str:admin_name>', views.AdministratorDetail.as_view()),
    path('permission/', views.PermissionList.as_view()),
    path('permission/<int:permission_id>', views.PermissionDetail.as_view())
]