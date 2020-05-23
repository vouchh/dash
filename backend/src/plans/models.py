from django.utils import timezone
from django.db import models
from accounts import helpers
from accounts.models import Account
from django_countries.fields import CountryField


class Plan(models.Model):

    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    default = models.BooleanField(default=False, unique=True)
    available = models.BooleanField(default=False)
    visible = models.BooleanField(default=False)
    trial_days= models.PositiveIntegerField(default=None, null=True)
    date_created = models.DateTimeField(default= timezone.now())
    customized = models.ForeignKey(Account, null=True, blank=True,on_delete=models.CASCADE)
    quotas = models.ManyToManyField('Quota', through='PlanQuota')
    url = models.URLField(max_length=200, blank=True)


class Period(models.Model):

    name = models.CharField(max_length=100)
    period_in_days = models.PositiveIntegerField(default=30)


class Currency(models.Model):
    name = models.CharField(max_length=3)
    friendly_name = models.CharField(max_length=50)
    symbol = models.CharField(max_length=20)


class PlanPeriod(models.Model):
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE)
    period = models.ForeignKey(Period, on_delete=models.CASCADE)
    currency = models.ForeignKey(Currency, default="USD", on_delete=models.DO_NOTHING)
    price = models.DecimalField(max_digits=7, decimal_places=2, db_index=True)


class BillingInfo(models.Model):

    account = models.OneToOneField(Account, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, db_index=True)
    address1 = models.CharField(max_length=200)
    address2 = models.CharField(max_length=200)
    zip = models.CharField(max_length=20)
    city = models.CharField(max_length=100)
    country = CountryField()


class PaymentMethod(models.Model):

    name = models.CharField(max_length=200, db_index=True)


class Subscription(models.Model):

    account = models.OneToOneField(Account, on_delete=models.CASCADE)
    plan_period = models.ForeignKey(PlanPeriod, on_delete=models.DO_NOTHING)
    started_at = models.DateTimeField(default= timezone.now())
    expires_at = models.DateField(blank=True)
    is_active = models.BooleanField(default=True)
    has_automatic_renewal = models.BooleanField(default=True)


class RecurringSubscription(models.Model):

    subscription = models.OneToOneField(Subscription, on_delete=models.CASCADE)
    token = models.CharField(max_length=255, default=None, blank=True,)
    payment_method = models.ForeignKey(PaymentMethod, on_delete=models.DO_NOTHING)


class Quota(models.Model):

    name = models.CharField(max_length=100)
    unit = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)
    is_boolean = models.BooleanField(default=False)


class PlanQuota(models.Model):
    plan = models.ForeignKey('Plan', on_delete=models.CASCADE)
    quota = models.ForeignKey('Quota', on_delete=models.CASCADE)
    value = models.IntegerField(default=1, null=True, blank=True)


class Order(models.Model):

    STATUS = [
        (1, 'NEW'),
        (2, 'COMPLETED'),
        (3, 'NOT_VALID'),
        (4, 'CANCELED'),
        (5, 'RETURNED'),
    ]

    account = models.ForeignKey(Account, on_delete=models.DO_NOTHING)
    subscription = models.ForeignKey('Subscription', on_delete=models.DO_NOTHING)
    date_created = models.DateTimeField(default= timezone.now())
    date_completed = models.DateTimeField(null=True)
    plan_extended_from = models.DateTimeField(default= timezone.now())
    plan_extended_until = models.DateTimeField(default= helpers.after_days(30))
    amount = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    tax = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)  # Tax=None is when tax is not applicable
    currency = models.CharField(max_length=3, default='USD')
    status = models.IntegerField(choices=STATUS, default=1)


class Invoice(models.Model):

    account = models.ForeignKey(Account, on_delete=models.DO_NOTHING)
    order = models.ForeignKey('Order', on_delete=models.DO_NOTHING)
    number = models.IntegerField()
    full_number = models.CharField(max_length=200)
    issued = models.DateField(db_index=True)
    payment_date = models.DateField(db_index=True)
    unit_price_net = models.DecimalField(max_digits=7, decimal_places=2)
    quantity = models.IntegerField(default=1)
    total_net = models.DecimalField(max_digits=7, decimal_places=2)
    total = models.DecimalField(max_digits=7, decimal_places=2)
    tax_total = models.DecimalField(max_digits=7, decimal_places=2)
    tax = models.DecimalField(max_digits=4, decimal_places=2, db_index=True, null=True,
                              blank=True)  # Tax=None is whet tax is not applicable
    rebate = models.DecimalField(max_digits=4, decimal_places=2, default=0)
    currency = models.CharField(max_length=3, default='USD')
    buyer_name = models.CharField(max_length=200)
    buyer_street = models.CharField(max_length=200)
    buyer_zipcode = models.CharField(max_length=200)
    buyer_city = models.CharField(max_length=200)
    buyer_country = CountryField(default='US')
    buyer_tax_number = models.CharField(max_length=200, blank=True)
    shipping_name = models.CharField(max_length=200)
    shipping_street = models.CharField(max_length=200)
    shipping_zipcode = models.CharField(max_length=200)
    shipping_city = models.CharField(max_length=200)
    shipping_country = CountryField(default='US')
    require_shipment = models.BooleanField(default=False, db_index=True)
    issuer_name = models.CharField(max_length=200)
    issuer_street = models.CharField(max_length=200)
    issuer_zipcode = models.CharField(max_length=200)
    issuer_city = models.CharField(max_length=200)
    issuer_country = CountryField(default='US')
    issuer_tax_number = models.CharField(max_length=200, blank=True, verbose_name=("TAX/VAT number"))
