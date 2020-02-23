# Generated by Django 2.2.3 on 2020-02-22 11:02

import book_issue.models
import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookIssue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('issue_uuid', models.CharField(default=book_issue.models.get_uuid, editable=False, max_length=36, unique=True, verbose_name='uuid')),
                ('issue_date', models.DateTimeField(default=datetime.datetime.now, verbose_name='issue date')),
                ('return_date', models.DateTimeField(default=datetime.datetime(2020, 3, 23, 11, 2, 32, 485130), verbose_name='return date')),
                ('fine_amount', models.IntegerField(default=0)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.Book')),
            ],
        ),
    ]