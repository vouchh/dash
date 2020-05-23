# Generated by Django 3.0.3 on 2020-05-22 08:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20200522_0819'),
        ('tickets', '0004_auto_20200522_0815'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attachment',
            name='account',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='accounts.Account'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='cannedresponse',
            name='account',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='accounts.Account'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='message',
            name='account',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='account_messages', to='accounts.Account'),
            preserve_default=False,
        ),
    ]
