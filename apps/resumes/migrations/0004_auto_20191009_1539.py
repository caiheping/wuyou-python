# Generated by Django 2.2.6 on 2019-10-09 07:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('resumes', '0003_auto_20191009_1030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resume',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='resumeworking',
            name='end_time',
            field=models.DateField(verbose_name='结束时间'),
        ),
    ]