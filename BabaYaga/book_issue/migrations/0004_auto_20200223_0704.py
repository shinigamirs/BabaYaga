# Generated by Django 2.2.3 on 2020-02-23 07:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_issue', '0003_auto_20200222_1529'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookissue',
            name='return_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 24, 7, 4, 32, 992526), verbose_name='return date'),
        ),
    ]
