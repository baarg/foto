# Generated by Django 3.2.8 on 2021-11-28 22:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0075_auto_20211129_0013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='imageDate',
            field=models.DateField(default=datetime.datetime(2021, 11, 29, 0, 14, 3, 216264)),
        ),
        migrations.AlterField(
            model_name='user',
            name='createdDate',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 29, 0, 14, 3, 211267)),
        ),
    ]
