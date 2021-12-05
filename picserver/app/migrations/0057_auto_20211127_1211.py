# Generated by Django 3.2.8 on 2021-11-27 10:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0056_auto_20211124_2315'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='usernameLikes',
            field=models.JSONField(default=[{}]),
        ),
        migrations.AlterField(
            model_name='image',
            name='imageDate',
            field=models.DateField(default=datetime.datetime(2021, 11, 27, 12, 11, 11, 797745)),
        ),
        migrations.AlterField(
            model_name='user',
            name='createdDate',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 27, 12, 11, 11, 796745)),
        ),
    ]