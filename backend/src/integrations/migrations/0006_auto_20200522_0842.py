# Generated by Django 3.0.3 on 2020-05-22 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('integrations', '0005_auto_20200522_0841'),
    ]

    operations = [
        migrations.AlterField(
            model_name='integration',
            name='date_cancelled',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='integration',
            name='date_updated',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
