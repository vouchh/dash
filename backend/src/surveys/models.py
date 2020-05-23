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
    date_created = models.DateTimeField(default=timezone.now)
    date_received = models.DateTimeField(null=True)
    date_updated = models.DateTimeField(null=True)


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
    date_created = models.DateTimeField(default=timezone.now)
    date_sent = models.DateTimeField(null=True)

