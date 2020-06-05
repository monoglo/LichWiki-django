"""newLichWiki URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url, include
from django.urls import path
from django.views.generic import TemplateView
from rest_framework import routers, permissions
from rest_framework.schemas import get_schema_view

from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="LichWiki API",
      default_version='v1',
      description="大学知识维基API文档",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="monoglo37@gmial.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include(router.urls)),
    path('api/', include([
        path('', include('subjects.urls')),
        path('', include('users.urls')),
        path('', include('administrators.urls')),
        path('', include('articles.urls')),
        path('', include('article_templates.urls')),
        path('', include('comments.urls')),
        path('', include('notifications.urls')),
        path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
        path('api/redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    ])),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
