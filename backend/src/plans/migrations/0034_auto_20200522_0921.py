# Generated by Django 3.0.3 on 2020-05-22 09:21

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('plans', '0033_auto_20200522_0920'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 22, 9, 21, 8, 576841, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='order',
            name='plan_extended_from',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 22, 9, 21, 8, 576877, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='order',
            name='plan_extended_until',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 21, 9, 21, 8, 576896, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='plan',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 22, 9, 21, 8, 572286, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='started_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 22, 9, 21, 8, 574962, tzinfo=utc)),
        ),
    ]