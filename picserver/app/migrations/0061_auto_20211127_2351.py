# Generated by Django 3.2.8 on 2021-11-27 21:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0060_auto_20211127_2351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='imageDate',
            field=models.DateField(default=datetime.datetime(2021, 11, 27, 23, 51, 15, 731097)),
        ),
        migrations.AlterField(
            model_name='user',
            name='createdDate',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 27, 23, 51, 15, 730098)),
        ),
    ]
