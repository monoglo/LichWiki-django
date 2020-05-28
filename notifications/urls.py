from django.urls import path
from . import views

app_name = 'notification'
urlpatterns = [
    path('notifications/<str:user_name>/amount', views.SelectNotificationAmountByUserID.as_view()),
    path('notifications/<str:user_name>/<int:u_id>', views.SelectNotificationListWithoutTextByUserID.as_view()),
    path('notifications/<int:n_id>', views.SelectNotificationDetailByNotificationID.as_view())
]