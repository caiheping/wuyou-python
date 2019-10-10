from django.db import models
from db.base_model import BaseModel

# Create your models here.


class Banner(BaseModel):
    index = models.IntegerField(default=1, verbose_name='索引')
    image = models.ImageField(upload_to='banner', verbose_name='图片')
    url = models.CharField(max_length=100, blank=True, null=True, verbose_name='链接地址')

    class Meta:
        verbose_name = '轮播图'
        verbose_name_plural = verbose_name


class AreaInfo(models.Model):
    """区域"""
    atitle = models.CharField(max_length=30)  # 名称
    aParent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)  # 关系

    def __str__(self):
        return self.atitle

    class Meta:
        verbose_name = '区域'
        verbose_name_plural = verbose_name
