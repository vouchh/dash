from rest_framework.decorators import api_view
from .models import Account
from .serializers import AccountSerializer
from rest_framework import viewsets


class AccountViewSet(viewsets.ModelViewSet):

    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    permission_classes = []
    authentication_classes = []
