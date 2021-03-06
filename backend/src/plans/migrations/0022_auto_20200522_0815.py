# Generated by Django 3.0.3 on 2020-05-22 08:15

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('plans', '0021_auto_20200522_0814'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 22, 8, 14, 52, 904208, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='order',
            name='plan_extended_from',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 22, 8, 14, 52, 904247, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='order',
            name='plan_extended_until',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 21, 8, 14, 52, 904266, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='plan',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 22, 8, 14, 52, 899647, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='started_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 22, 8, 14, 52, 902284, tzinfo=utc)),
        ),
    ]
