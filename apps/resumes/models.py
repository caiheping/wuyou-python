from django.db import models
from db.base_model import BaseModel
from users.models import Users
from DjangoUeditor.models import UEditorField

# Create your models here.


class Resume(BaseModel):
    """简历"""
    Is_Open = (
        (0, '不公开'),
        (1, '公开')
    )
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    name = models.CharField(max_length=30, verbose_name='简历名称')
    is_open = models.IntegerField(choices=Is_Open, default=0, verbose_name='是否公开')
    progress = models.IntegerField(default=0, verbose_name='完善进度')
    username = models.CharField(max_length=30, verbose_name='简历用户名')
    pic = models.ImageField(upload_to='resumes/', verbose_name='照片')
    sex = models.CharField(max_length=6, choices=(('male', '男'), ('female', '女')), default='female', verbose_name='性别')
    birthday = models.DateField(null=True, blank=True, verbose_name='出生年月')
    phone = models.CharField(max_length=11, blank=True, null=True, verbose_name='电话')
    status = models.IntegerField(choices=((1, '在职'), (0, '离职')), default=0, verbose_name='状态')
    start_working = models.DateField(null=True, blank=True, verbose_name='开始工作时间')
    addr = models.CharField(max_length=30, verbose_name='地址')
    email = models.EmailField(max_length=100, null=True, blank=True, verbose_name='邮箱')
    ID_number = models.CharField(max_length=18, blank=True, null=True, verbose_name='身份证号')
    annual_income = models.IntegerField(default=0, verbose_name='年收入')
    hukou_or_nationality = models.CharField(max_length=20, blank=True, null=True, verbose_name='户口/国籍')
    marital_status = models.IntegerField(choices=((0, '未婚'), (1, '已婚')), default=0, verbose_name='婚姻状况')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '简历'
        verbose_name_plural = verbose_name


class ResumeWorking(BaseModel):
    """工作经验"""
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)
    start_time = models.DateField(verbose_name='开始时间')
    end_time = models.DateField(verbose_name='介绍时间')
    company = models.CharField(max_length=30, verbose_name='公司')
    position = models.CharField(max_length=20, verbose_name='职位')
    job_description = UEditorField(blank=True, verbose_name='工作描述')
    industry = models.CharField(max_length=100, blank=True, null=True, verbose_name='行业')
    department = models.CharField(max_length=30, blank=True, null=True, verbose_name='部门')
    nature = models.CharField(max_length=30, blank=True, null=True, verbose_name='性质')
    other = models.CharField(max_length=30, blank=True, null=True, verbose_name='其他')
    type = models.CharField(max_length=30, blank=True, null=True, verbose_name='类型')

    def __str__(self):
        return self.company

    class Meta:
        verbose_name = '工作经验'
        verbose_name_plural = verbose_name


class ResumeEducation(BaseModel):
    """教育经历"""
    Education_TYPE = (
        (1, "高中"),
        (2, "大专"),
        (3, "本科"),
        (4, "硕士"),
    )
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)
    enrollment_time = models.DateField(verbose_name='入学时间')
    graduation_time = models.DateField(verbose_name='毕业时间')
    school = models.CharField(max_length=30, verbose_name='学校')
    education = models.IntegerField(choices=Education_TYPE, verbose_name='学历')
    major = models.CharField(max_length=30, verbose_name='专业')
    major_desc = models.CharField(max_length=100, blank=True, null=True, verbose_name='专业描述')
    is_overseas_study = models.IntegerField(choices=((0, '否'), (1, '是')), default=0, verbose_name='是否留学')

    def __str__(self):
        return self.school

    class Meta:
        verbose_name = '教育经历'
        verbose_name_plural = verbose_name


class ResumeJob(BaseModel):
    """求职意向"""
    PayType = (
        (1, '月薪'),
        (2, '年薪'),
    )
    ArrivalTime = (
        (1, '随时'),
        (2, '一周内'),
        (3, '一个月内'),
    )
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)
    place = models.CharField(max_length=30, verbose_name='地点')
    function = UEditorField(blank=True, verbose_name='职能')
    pay_type = models.IntegerField(choices=PayType, default=1, verbose_name='薪资类型')
    salary_expectation = models.IntegerField(verbose_name='期望薪资')
    work_type = models.CharField(max_length=30, blank=True, null=True, verbose_name='工作类型')
    industry = models.CharField(max_length=30, blank=True, null=True, verbose_name='行业')
    arrival_time = models.IntegerField(choices=ArrivalTime, default=1, verbose_name='到岗时间')
    self_evaluation = UEditorField(blank=True, verbose_name='自我评价')
    personal_tags = models.CharField(max_length=30, blank=True, null=True, verbose_name='个人标签')

    def __str__(self):
        return self.place

    class Meta:
        verbose_name = '求职意向'
        verbose_name_plural = verbose_name


class ResumeProjectExperience(BaseModel):
    """项目经验"""
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)
    start_time = models.DateField(verbose_name='开始时间')
    end_time = models.DateField(verbose_name='结束时间')
    name = models.CharField(max_length=30, verbose_name='项目名称')
    project_description = UEditorField(blank=True, verbose_name='项目描述')
    responsibility_description = UEditorField(blank=True, verbose_name='责任描述')
    affiliated_company = models.CharField(max_length=30, blank=True, null=True, verbose_name='所属公司')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '项目经验'
        verbose_name_plural = verbose_name
