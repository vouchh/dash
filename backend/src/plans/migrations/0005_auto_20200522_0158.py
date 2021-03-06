# Generated by Django 3.0.3 on 2020-05-22 01:58

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('plans', '0004_auto_20200522_0153'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 22, 1, 57, 59, 698459, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='order',
            name='plan_extended_from',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 22, 1, 57, 59, 698489, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='order',
            name='plan_extended_until',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 21, 1, 57, 59, 698502, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='plan',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 22, 1, 57, 59, 694586, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='started_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 22, 1, 57, 59, 696844, tzinfo=utc)),
        ),
    ]
