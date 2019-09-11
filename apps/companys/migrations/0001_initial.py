# Generated by Django 2.2.1 on 2019-09-10 09:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Companys',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('is_delete', models.BooleanField(default=False, verbose_name='删除标记')),
                ('name', models.CharField(max_length=30, verbose_name='公司名')),
                ('type', models.IntegerField(choices=[(1, '国企'), (2, '外企'), (3, '民营')], help_text='公司类型', verbose_name='公司类型')),
                ('addr', models.CharField(max_length=100, verbose_name='地址')),
                ('introduce', models.TextField(blank=True, null=True, verbose_name='介绍')),
                ('personnel', models.IntegerField(default=0, verbose_name='人员')),
                ('company_start_time', models.DateField(blank=True, null=True, verbose_name='成立时间')),
            ],
            options={
                'verbose_name': '公司',
                'verbose_name_plural': '公司',
            },
        ),
        migrations.CreateModel(
            name='Welfare',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('is_delete', models.BooleanField(default=False, verbose_name='删除标记')),
                ('name', models.CharField(max_length=20, verbose_name='名称')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='companys.Companys')),
            ],
            options={
                'verbose_name': '福利',
                'verbose_name_plural': '福利',
            },
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('is_delete', models.BooleanField(default=False, verbose_name='删除标记')),
                ('job', models.CharField(max_length=20, verbose_name='职业')),
                ('min_salary', models.IntegerField(verbose_name='最小薪水')),
                ('max_salary', models.IntegerField(verbose_name='最大薪水')),
                ('describe', models.TextField(verbose_name='描述')),
                ('working_years', models.IntegerField(verbose_name='工龄')),
                ('education', models.IntegerField(choices=[(1, '高中'), (2, '大专'), (3, '本科'), (4, '硕士')], verbose_name='学历')),
                ('recruitment', models.IntegerField(default=1, verbose_name='招聘人数')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='companys.Companys')),
            ],
            options={
                'verbose_name': '职业',
                'verbose_name_plural': '职业',
            },
        ),
    ]
