# Generated by Django 3.0.6 on 2020-05-23 21:23

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('plans', '0035_auto_20200522_1304'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 23, 21, 23, 38, 312867, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='order',
            name='plan_extended_from',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 23, 21, 23, 38, 312899, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='order',
            name='plan_extended_until',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 22, 21, 23, 38, 312946, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='plan',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 23, 21, 23, 38, 308923, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='started_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 23, 21, 23, 38, 311174, tzinfo=utc)),
        ),
    ]
