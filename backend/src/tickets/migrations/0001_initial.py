# Generated by Django 3.0.3 on 2020-05-21 10:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
        ('integrations', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AddressInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('address_channel', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='integrations.Integration')),
            ],
        ),
        migrations.CreateModel(
            name='Attachment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='')),
                ('file_name', models.CharField(max_length=100)),
                ('file_type', models.CharField(max_length=100)),
                ('size', models.IntegerField()),
                ('path', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='CannedResponse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('is_available_to_all', models.BooleanField(default=True)),
                ('subject', models.CharField(max_length=200)),
                ('body', models.TextField()),
                ('attachments', models.ManyToManyField(to='tickets.Attachment')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Intent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('send_status', models.IntegerField(choices=[(1, 'New'), (2, 'Sent'), (3, 'Failed'), (4, 'Permanently Failed')])),
                ('subject', models.CharField(max_length=100)),
                ('body', models.TextField()),
                ('body_text', models.TextField()),
                ('by_agent', models.BooleanField(default=False)),
                ('created_through', models.CharField(max_length=100)),
                ('mail_headers', models.TextField()),
                ('rule_id', models.IntegerField(null=True)),
                ('external_id', models.CharField(max_length=100)),
                ('sender_ip', models.GenericIPAddressField()),
                ('reason_for_failure', models.TextField()),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('date_opened', models.DateTimeField(null=True)),
                ('date_failed', models.DateTimeField(null=True)),
                ('attachments', models.ManyToManyField(to='tickets.Attachment')),
                ('canned_response_used', models.ManyToManyField(to='tickets.CannedResponse')),
                ('from_address', models.ManyToManyField(related_name='from_address', to='tickets.AddressInfo')),
                ('integration', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='integrations.Integration')),
                ('sent_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sent_by', to=settings.AUTH_USER_MODEL)),
                ('sent_to', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='sent_to', to=settings.AUTH_USER_MODEL)),
                ('signature_used', models.ManyToManyField(to='users.Signature')),
                ('to_address', models.ManyToManyField(related_name='to_address', to='tickets.AddressInfo')),
            ],
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField(choices=[(1, 'Public'), (2, 'Private')])),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=400)),
                ('status', models.IntegerField(choices=[(1, 'Open'), (2, 'Closed')], default=1)),
                ('by_agent', models.BooleanField(default=False)),
                ('has_priority', models.BooleanField(default=False)),
                ('is_spam', models.BooleanField(default=False)),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('date_closed', models.DateTimeField(null=True)),
                ('date_updated', models.DateTimeField(null=True)),
                ('assigned_to_team', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.Team')),
                ('assigned_to_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='assigned_to_user', to=settings.AUTH_USER_MODEL)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='created_by', to=settings.AUTH_USER_MODEL)),
                ('integration', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='integrations.Integration')),
                ('messages', models.ManyToManyField(to='tickets.Message')),
                ('notes', models.ManyToManyField(to='tickets.Note')),
                ('tags', models.ManyToManyField(to='tickets.Tag')),
            ],
        ),
        migrations.AddField(
            model_name='cannedresponse',
            name='tags',
            field=models.ManyToManyField(to='tickets.Tag'),
        ),
    ]