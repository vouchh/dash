from rest_framework.decorators import api_view
from .models import Team
from .serializers import TeamSerializer
from rest_framework import viewsets


class TeamViewSet(viewsets.ModelViewSet):

    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    permission_classes = []
    authentication_classes = []
