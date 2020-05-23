# Generated by Django 3.0.3 on 2020-05-21 10:30

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField(choices=[(1, 'Active'), (2, 'Suspended'), (3, 'Cancelled')])),
                ('is_suspended', models.BooleanField(default=True)),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('date_suspended', models.DateTimeField(null=True)),
                ('date_cancelled', models.DateTimeField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='AccountSettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]