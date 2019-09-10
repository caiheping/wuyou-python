from django.db import models
from db.base_model import BaseModel

# Create your models here.


class Banner(BaseModel):
    index = models.IntegerField(verbose_name='索引')
    image = models.CharField(max_length=100, verbose_name='图片')
    url = models.CharField(max_length=100, verbose_name='链接地址')

    class Meta:
        verbose_name = '轮播图'
        verbose_name_plural = verbose_name
