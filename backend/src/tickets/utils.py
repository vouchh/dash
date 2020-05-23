from django.utils import timezone
from rest_framework.decorators import api_view


def create_ticket(request):

    account_id = request.account_id
