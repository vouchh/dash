from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django_countries.fields import CountryField
from integrations.models import Integration
from accounts.models import Account


class Signature(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    body = models.TextField()
    integration = models.ForeignKey(Integration, on_delete=models.SET_NULL, null=True, related_name="signatures")
    date_created = models.DateTimeField(default=timezone.now)
    date_closed = models.DateTimeField(null=True)


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

    account = models.ForeignKey(Account, on_delete=models.CASCADE, null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics', )
    address1 = models.CharField(max_length=200, default='')
    address2 = models.CharField(max_length=200, default='', blank=True)
    bio = models.TextField()
    phone = models.CharField(max_length=25, default='', blank=True)
    city = models.CharField(max_length=150, default='')
    state = models.CharField(max_length=50, default='')
    zip = models.CharField(max_length=10, default='')
    country = CountryField()
    is_active = models.BooleanField(default=True)
    is_customer = models.BooleanField(default=True)
    roles = models.ManyToManyField(Role)


class Agent(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    badges = models.ManyToManyField(Badge)


class Team(models.Model):

    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name="teams", null=True, blank=True)
    name = models.CharField(max_length=100)
    agents = models.ManyToManyField(Agent)
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    date_created = models.DateTimeField(default=timezone.now)