from django.db import models
from db.base_model import BaseModel
from DjangoUeditor.models import UEditorField



# Create your models here.


class Companys(BaseModel):
    """公司"""
    Company_TYPE = (
        (1, "国企"),
        (2, "外企"),
        (3, "民营"),
    )
    name = models.CharField(max_length=30, verbose_name='公司名')
    type = models.IntegerField(choices=Company_TYPE, verbose_name="公司类型", help_text="公司类型")
    addr = models.CharField(max_length=100, verbose_name='详细地址')
    area = models.CharField(max_length=30, blank=True, null=True, verbose_name='区域')
    introduce = UEditorField(blank=True, verbose_name='介绍')
    personnel = models.IntegerField(default=1, verbose_name='人员')
    company_start_time = models.DateField(null=True, blank=True, verbose_name="成立时间")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '公司'
        verbose_name_plural = verbose_name


class Job(BaseModel):
    """职业"""
    Education_TYPE = (
        (1, "高中"),
        (2, "大专"),
        (3, "本科"),
        (4, "硕士"),
    )
    job = models.CharField(max_length=20, verbose_name='职业')
    company = models.ForeignKey(Companys, on_delete=models.CASCADE)
    min_salary = models.IntegerField(verbose_name='最小薪水')
    max_salary = models.IntegerField(verbose_name='最大薪水')
    describe = UEditorField(blank=True, verbose_name='描述')
    working_years = models.IntegerField(verbose_name='工龄')
    education = models.IntegerField(choices=Education_TYPE, verbose_name='学历')
    recruitment = models.IntegerField(default=1, verbose_name='招聘人数')

    def __str__(self):
        return self.job

    class Meta:
        verbose_name = '职业'
        verbose_name_plural = verbose_name


class Welfare(BaseModel):
    """福利"""
    name = models.CharField(max_length=20, verbose_name='名称')
    company = models.ForeignKey(Companys, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '福利'
        verbose_name_plural = verbose_name
