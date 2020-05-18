from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User



class HappinessSurvey(models.Model):
    subject: models.CharField(max_length=100)
    body: models.TextField()
    body_text: models.TextField()
    ticket_id: models.IntegerField()
    score: models.IntegerField()
    agent_id :  models.IntegerField()
    customer_id :  models.IntegerField()
    reason: models.TextField()


class ReviewSite(models.Model):

    name = models.CharField(max_length=100)
    url = models.URLField()


class ReviewRequest(models.Model):
    subject: models.CharField(max_length=100)
    body: models.TextField()
    body_text: models.TextField()
    customer: models.ForeignKey(User, on_delete=models.DO_NOTHING)
    review_site: models.ManyToManyField(ReviewSite)
    ticket_id :  models.IntegerField()
    reason: models.TextField()


class SubscriptionPackage(models.Model):
    name: models.CharField(max_length=100)
    description: models.TextField()


class Subscription(models.Model):
    package = models.ForeignKey(SubscriptionPackage, on_delete=models.DO_NOTHING)


class IntegrationType(models.Model):
    name: models.CharField(max_length=100)
    website: models.URLField()


class Integration(models.Model):

    is_active = models.BooleanField(default=True)
    type = models.ForeignKey(IntegrationType, on_delete=models.DO_NOTHING)
    icon = models.ImageField()
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    date_created = models.DateTimeField(default=timezone.now)
    date_cancelled  = models.DateTimeField(null=True)
    date_updated = models.DateTimeField(null=True)


class Channel(models.Model):

    name = models.CharField(max_length=100)


class Attachment(models.Model):

    file_name = models.CharField(max_length=100)
    file_type = models.CharField(max_length=100)
    size = models.IntegerField()
    path = models.CharField(max_length=100)


class Tag(models.Model):

    name = models.CharField(max_length=100)


class Notes(models.Model):
    class Status(models.IntegerChoices):
        PUBLIC = 1
        PRIVATE = 2

    status = models.IntegerField(choices=Status.choices)
    content: models.CharField(max_length=100)
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    ticket = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(default=timezone.now)


class Team(models.Model):

    name = models.CharField(max_length=100)
    users = models.ManyToManyField(User)
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    date_created = models.DateTimeField(default=timezone.now)


class Badge(models.Model):

    name = models.CharField(max_length=100)
    icon = models.ImageField()
    description = models.TextField()
    date_created = models.DateTimeField(default=timezone.now)


class Role(models.Model):

    ROLE_CHOICES = [
        ('super_admin', 'Super Admin'),
        ('admin', 'Admin'),
        ('agent', 'Agent'),
        ('end_user', 'End-User'),
        ('staff', 'Staff'),
    ]

    type = models.IntegerField(choices=ROLE_CHOICES, default= "end_user")
    description = models.CharField(max_length=200, default='')


class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics', )
    address1 = models.CharField(max_length=200, default='')
    address2 = models.CharField(max_length=200, default='', blank=True)
    bio = models.TextField()
    phone = models.CharField(max_length=25, default='', blank=True)
    city = models.CharField(max_length=150, default='')
    state = models.CharField(max_length=50, default='')
    zip = models.CharField(max_length=10, default='')
    country = models.country()
    is_active = models.BooleanField(default=True)
    is_customer = models.BooleanField(default=True)
    badges = models.ManyToManyField(Badge)
    roles = models.ManyToManyField(Role)


class AddressBook(models.Model):
    address = models.CharField(max_length=100)
    address_channel = models.ForeignKey(Channel, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=100)


class Intent(models.Model):

    name = models.CharField(max_length=100)


class CannedResponse(models.Model):
    name = models.CharField(max_length=100)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    is_available_to_all = models.BooleanField(default=True)
    subject = models.CharField(max_length=200)
    body = models.TextField()
    attachments = models.ManyToManyField(Attachment)
    tags = models.ManyToManyField(Tag)


class Signature(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    integration = models.ForeignKey(Integration, on_delete=models.SET_NULL, null=True)
    date_created = models.DateTimeField(default=timezone.now)
    date_closed = models.DateTimeField(null=True)


class Message(models.Model):

    class SendStatus(models.IntegerChoices):
        NEW = 1
        SENT = 2
        FAILED = 3
        PERMANENTLY_FAILED = 4

    send_status = models.IntegerField(choices=SendStatus.choices)
    subject = models.CharField(max_length=100)
    body = models.TextField()
    body_text = models.TextField()
    attachments = models.ManyToManyField(Attachment)
    by_agent = models.BooleanField(default=False)
    created_through = models.CharField(max_length=100)
    mail_headers = models.TextField()
    sent_by = models.ForeignKey(User, on_delete=models.CASCADE)
    sent_to = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    channel = models.ForeignKey(Channel, on_delete=models.DO_NOTHING)
    rule_id = models.IntegerField(null=True)
    canned_response_used = models.ManyToManyField(CannedResponse) #data field
    integration = models.ForeignKey(Integration, models.SET_NULL, null=True)
    signature_used = models.ManyToManyField(Signature) #data field
    external_id = models.CharField(max_length=100) # id of the exeternal service where the message was received.
    to_address = models.ManyToManyField(AddressBook)
    from_address = models.ManyToManyField(AddressBook)
    sender_ip = models.GenericIPAddressField()
    reason_for_failure = models.TextField()
    date_created = models.DateTimeField(default=timezone.now)
    date_opened = models.DateTimeField(null=True)
    date_failed = models.DateTimeField(null=True)


class Ticket(models.Model):

    class Status(models.IntegerChoices):
        OPEN = 1
        CLOSED = 2

    subject = models.CharField(max_length=400) # if null - subject of the first ticket message
    status = models.IntegerField(choices=Status.choices)
    channel = models.ForeignKey(Channel, on_delete=models.DO_NOTHING)
    messages = models.ManyToManyField(Message)
    assigned_to_user = models.ForeignKey(User, models.SET_NULL, null=True)
    assigned_to_team = models.ForeignKey(Team, models.SET_NULL, null=True)
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    by_agent = models.BooleanField(default=False)
    has_priority = models.BooleanField(default=False)
    is_spam = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag)
    integration = models.ForeignKey(Integration, models.SET_NULL, null=True)
    date_created = models.DateTimeField(default=timezone.now)
    date_closed  = models.DateTimeField(null=True)
    date_updated = models.DateTimeField(null=True)

    def __str__(self):
        return self.subject


class Account(models.Model):
    class Status(models.IntegerChoices):
        ACTIVE = 1
        SUSPENDED = 2
        CANCELLED = 3

    status = models.IntegerField(choices=Status.choices)
    is_suspended = models.BooleanField(default=True)
    owner: models.ForeignKey(User, on_delete=models.DO_NOTHING)
    company_name: models.CharField(max_length=100)
    email: models.EmailField()
    phone: models.CharField(max_length=100)
    domain: models.CharField(max_length=100)
    subscription: models.ForeignKey(Subscription, on_delete=models.DO_NOTHING)
    tickets: models.ManyToManyField(Ticket)
    canned_responses : models.ManyToManyField(CannedResponse)
    teams: models.ManyToManyField(Team)
    attachments: models.ManyToManyField(Attachment)
    integrations: models.ManyToManyField(Integration)
    review_requests: models.ManyToManyField(ReviewRequest)
    users: models.ManyToManyField(User, on_delete = models.CASCADE)
    subscription: models.OneToOneField(Subscription, on_delete=models.CASCADE)
    date_created = models.DateTimeField(default=timezone.now)
    date_suspended = models.DateTimeField(null=True)
    date_cancelled = models.DateTimeField(null=True)
