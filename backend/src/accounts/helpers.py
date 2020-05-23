from django.utils import timezone
from django.conf import settings
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from tickets.models import Ticket
import json


def after_days(days):
    return timezone.now() + timezone.timedelta(days=days)

def is_email(email):
    try:
        validate_email(email)
        return True
    except ValidationError:
        return False

def clean_request(request):
    request = request.body.decode('utf-8')
    request = json.loads(request)
    return request

def set_ticket_status(ticket_id, status):
    ticket = Ticket.objects.get(id=ticket_id)
    ticket.status = status
    ticket.save()
    return True
