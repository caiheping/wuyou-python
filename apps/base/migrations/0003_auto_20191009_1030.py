# Generated by Django 2.2.1 on 2019-10-09 02:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_auto_20191008_1435'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banner',
            name='image',
            field=models.ImageField(upload_to='banner/', verbose_name='图片'),
        ),
    ]
