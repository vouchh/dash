from rest_framework.decorators import api_view
from .models import Integration
from .serializers import IntegrationSerializer
from rest_framework import viewsets



class IntegrationViewSet(viewsets.ModelViewSet):

    queryset = Integration.objects.all()
    serializer_class = IntegrationSerializer
    permission_classes = []
    authentication_classes = []
