# Generated by Django 3.0.3 on 2020-05-22 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('integrations', '0006_auto_20200522_0842'),
    ]

    operations = [
        migrations.AlterField(
            model_name='integrationtype',
            name='icon',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
