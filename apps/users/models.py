from django.db import models
from django.contrib.auth.models import AbstractUser
from db.base_model import BaseModel
# Create your models here.


class Users(AbstractUser, BaseModel):
    """用户模型类"""
    area = models.CharField(max_length=30, blank=True, null=True, verbose_name='用户所在区域')

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'df_user'
        verbose_name = '用户'
        verbose_name_plural = verbose_name
