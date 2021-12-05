# Generated by Django 3.2.8 on 2021-11-09 13:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0024_auto_20211109_1500'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='emailActvate',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='image',
            name='imageDate',
            field=models.DateField(default=datetime.datetime(2021, 11, 9, 15, 3, 30, 87037)),
        ),
        migrations.AlterField(
            model_name='user',
            name='birthDate',
            field=models.DateField(default=datetime.datetime(2021, 11, 9, 15, 3, 30, 86038)),
        ),
        migrations.AlterField(
            model_name='user',
            name='createdDate',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 9, 15, 3, 30, 86038)),
        ),
    ]
