# coding:utf-8
from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)                    # title
    category = models.CharField(max_length=50, blank=True)      # 标签
    date_time = models.DateTimeField(auto_now_add=True)         # date
    content = models.TextField(blank=True, null=True)           # 正文

    def __unicode__(self):
        return self.title               # 显示博客题目

    class Meta:
        ordering = ['-date_time']       # 按时间下降排序