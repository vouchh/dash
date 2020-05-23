from django.db import models
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from surveys.models import ReviewRequest
from timezone_field import TimeZoneFormField


class Account(models.Model):
    class Status(models.IntegerChoices):
        ACTIVE = 1
        SUSPENDED = 2
        CANCELLED = 3

    status = models.IntegerField(choices=Status.choices)
    owner = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    company_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    domain = models.CharField(max_length=100)
    date_created = models.DateTimeField(default=timezone.now)
    date_suspended = models.DateTimeField(null=True, blank=True)
    date_cancelled = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.company_name


class AccountSettings(models.Model):
    account = models.OneToOneField(Account, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    timezone = TimeZoneFormField()
