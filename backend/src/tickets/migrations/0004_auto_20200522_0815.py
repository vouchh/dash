# Generated by Django 3.0.3 on 2020-05-22 08:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
        ('tickets', '0003_auto_20200522_0814'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='account',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='account_tickets', to='accounts.Account'),
            preserve_default=False,
        ),
    ]
