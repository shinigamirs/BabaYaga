# Generated by Django 2.2.3 on 2020-02-22 15:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_issue', '0002_bookissue_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookissue',
            name='return_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 23, 15, 29, 25, 240542), verbose_name='return date'),
        ),
    ]