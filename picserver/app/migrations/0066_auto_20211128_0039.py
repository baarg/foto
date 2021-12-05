# Generated by Django 3.2.8 on 2021-11-27 22:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0065_auto_20211128_0035'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Gener',
            new_name='Tag',
        ),
        migrations.RenameField(
            model_name='tag',
            old_name='type',
            new_name='tagName',
        ),
        migrations.AlterField(
            model_name='image',
            name='imageDate',
            field=models.DateField(default=datetime.datetime(2021, 11, 28, 0, 39, 5, 597551)),
        ),
        migrations.AlterField(
            model_name='user',
            name='createdDate',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 28, 0, 39, 5, 595552)),
        ),
    ]