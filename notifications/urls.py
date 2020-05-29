from django.urls import path
from . import views

app_name = 'notification'
urlpatterns = [
    path('notifications', views.CreateNotification.as_view()),
    path('notifications/user/<str:user_name>/amount', views.SelectUnreadNotificationAmountByUserID.as_view()),
    path('notifications/user/<str:user_name>', views.SelectAllNotificationWithoutTextByUserName.as_view()),
    path('notifications/id/<int:n_id>', views.SelectNotificationDetailByNotificationID.as_view())
]