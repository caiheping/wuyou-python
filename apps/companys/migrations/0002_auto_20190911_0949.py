# Generated by Django 2.2.1 on 2019-09-11 01:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('companys', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='companys',
            name='area',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='区域'),
        ),
        migrations.AlterField(
            model_name='companys',
            name='addr',
            field=models.CharField(max_length=100, verbose_name='详细地址'),
        ),
        migrations.CreateModel(
            name='AreaInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('atitle', models.CharField(max_length=30)),
                ('aParent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='companys.AreaInfo')),
            ],
            options={
                'verbose_name': '区域',
                'verbose_name_plural': '区域',
            },
        ),
    ]