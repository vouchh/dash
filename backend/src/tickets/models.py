from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from integrations.models import Integration
from users.models import Signature, Team
from accounts.models import Account


import string


class Attachment(models.Model):

    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    file = models.FileField()
    file_name = models.CharField(max_length=100)
    file_type = models.CharField(max_length=100)
    size = models.IntegerField()
    path = models.CharField(max_length=100)

    def __str__(self):
        return self.file_name


class Tag(models.Model):

    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class AddressInfo(models.Model):
    address = models.CharField(max_length=100)
    address_channel = models.ForeignKey(Integration, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Intent(models.Model):

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class CannedResponse(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    is_available_to_all = models.BooleanField(default=True)
    subject = models.CharField(max_length=200)
    body = models.TextField()
    attachments = models.ManyToManyField(Attachment)
    tags = models.ManyToManyField(Tag)


class Ticket(models.Model):

    class Status(models.IntegerChoices):
        OPEN = 1
        CLOSED = 2

    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='account_tickets')
    subject = models.CharField(max_length=400, blank=True) # if null - subject of the first ticket message
    status = models.IntegerField(choices=Status.choices, default=1)
    assigned_to_user = models.ForeignKey(User, null=True, blank=True, on_delete=models.DO_NOTHING, related_name='assigned_tickets')
    assigned_to_team = models.ForeignKey(Team, blank=True, null=True, on_delete=models.DO_NOTHING, related_name='assigned_team_tickets')
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='created_by')
    by_agent = models.BooleanField(default=False)
    has_priority = models.BooleanField(default=False)
    is_spam = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag, blank=True)
    integration = models.ForeignKey(Integration, null=True, blank=True, on_delete=models.DO_NOTHING)
    date_created = models.DateTimeField(default=timezone.now)
    date_closed = models.DateTimeField(null=True, blank=True)
    date_updated = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.subject

    def notes(self):
        notes = Note.objects.filter(ticket=self)
        return notes.values()

    def messages(self):
        return self.messages.values()


class Message(models.Model):

    class SendStatus(models.IntegerChoices):
        NEW = 1
        SENT = 2
        FAILED = 3
        PERMANENTLY_FAILED = 4

    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='message_accounts')
    send_status = models.IntegerField(choices=SendStatus.choices)
    ticket = models.ForeignKey(Ticket, related_name='messages', on_delete=models.CASCADE, blank=True, null=True)
    subject = models.CharField(max_length=100, blank=True)
    body_html = models.TextField(blank=True)
    body_text = models.TextField(blank=True)
    attachments = models.ManyToManyField(Attachment, blank=True)
    by_agent = models.BooleanField(default=False)
    created_through = models.CharField(max_length=100, default= 'email')
    mail_headers = models.TextField(blank=True)
    sent_by = models.ForeignKey(User, related_name='sent_by', on_delete=models.CASCADE)
    sent_to = models.ForeignKey(User, related_name='sent_to', on_delete=models.DO_NOTHING)
    rule_id = models.IntegerField(null=True, blank=True)
    canned_response_used = models.ManyToManyField(CannedResponse, blank=True) #data field
    integration = models.ForeignKey(Integration, models.SET_NULL, null=True, blank=True)
    signature_used = models.ManyToManyField(Signature, blank=True) #data field
    external_id = models.CharField(max_length=100, blank=True) # id of the exeternal service where the message was received.
    to_address = models.ManyToManyField(AddressInfo, related_name='to_address', blank=True)
    from_address = models.ManyToManyField(AddressInfo, related_name='from_address', blank=True)
    sender_ip = models.GenericIPAddressField(blank=True, null=True)
    reason_for_failure = models.TextField(blank=True)
    date_created = models.DateTimeField(default=timezone.now)
    date_opened = models.DateTimeField(null=True, blank=True)
    date_failed = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        if self.subject:
            return self.subject
        return self.body_html[0:50]+'...'


class Note(models.Model):
    class Status(models.IntegerChoices):
        PUBLIC = 1
        PRIVATE = 2

    status = models.IntegerField(choices=Status.choices)
    content = models.TextField()
    ticket = models.ForeignKey(Ticket, related_name='notes_tickets', on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.content[0:50]+'...'
