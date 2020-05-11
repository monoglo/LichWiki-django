from django.db import models
from subjects.models import Subject
from users.models import User

# Create your models here.


class Article(models.Model):
    a_id = models.AutoField(primary_key=True)
    a_subject = models.ForeignKey(Subject, null=True, on_delete=models.SET_NULL)
    a_author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    a_title = models.CharField(max_length=128)
    a_text = models.TextField(null=True)
    a_length = models.IntegerField(default=0)
    a_create_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.a_title


class ArticleHistory(models.Model):
    ah_id = models.AutoField(primary_key=True)
    ah_article = models.ForeignKey(Article, null=True, on_delete=models.SET_NULL)
    ah_author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    ah_summary = models.CharField(max_length=256, null=True)
    ah_title = models.CharField(max_length=128)
    ah_text = models.TextField(null=True)
    ah_length = models.IntegerField(default=0)
    ah_edit_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.ah_summary
