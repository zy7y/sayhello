from django.db import models

# Create your models here.
from django.utils import timezone


class Text(models.Model):
    name = models.CharField(max_length=60, verbose_name="昵称")
    body = models.CharField(max_length=200, verbose_name="内容")
    create_at = models.DateTimeField(default=timezone.now, verbose_name="创建时间")

    class Meta:
        verbose_name = "留言"
        verbose_name_plural = "留言管理"

    def __str__(self):
        return ""
