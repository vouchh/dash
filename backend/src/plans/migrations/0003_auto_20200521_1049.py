# Generated by Django 3.0.3 on 2020-05-21 10:49

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('plans', '0002_auto_20200521_1049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 21, 10, 49, 34, 289613, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='order',
            name='plan_extended_from',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 21, 10, 49, 34, 289644, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='order',
            name='plan_extended_until',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 20, 10, 49, 34, 289657, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='plan',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 21, 10, 49, 34, 285728, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='started_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 21, 10, 49, 34, 287981, tzinfo=utc)),
        ),
    ]
