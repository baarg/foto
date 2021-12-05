# Generated by Django 3.2.8 on 2021-11-13 12:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0041_auto_20211113_1409'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='publicImages'),
        ),
        migrations.AlterField(
            model_name='image',
            name='imageDate',
            field=models.DateField(default=datetime.datetime(2021, 11, 13, 14, 18, 45, 440152)),
        ),
        migrations.AlterField(
            model_name='user',
            name='createdDate',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 13, 14, 18, 45, 439151)),
        ),
        migrations.DeleteModel(
            name='PerUser',
        ),
    ]
