# Generated by Django 3.2.8 on 2021-11-09 13:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0022_auto_20211109_1459'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='createdDate',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 9, 15, 0, 11, 803884)),
        ),
        migrations.AlterField(
            model_name='image',
            name='imageDate',
            field=models.DateField(default=datetime.datetime(2021, 11, 9, 15, 0, 11, 805883)),
        ),
        migrations.AlterField(
            model_name='user',
            name='birthDate',
            field=models.DateField(default=datetime.datetime(2021, 11, 9, 15, 0, 11, 803884)),
        ),
    ]
