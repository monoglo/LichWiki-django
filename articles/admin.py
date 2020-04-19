from django.contrib import admin
from .models import Article, ArticleHistory
# Register your models here.

admin.site.register(Article)
admin.site.register(ArticleHistory)
