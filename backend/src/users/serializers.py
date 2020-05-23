from rest_framework import serializers
from .models import Team
from django.utils import timezone


class TeamSerializer(serializers.ModelSerializer):

    class Meta:
        model = Team
        fields = ['id', 'name', 'account', 'agents', 'created_by', 'date_created']
        read_only_fields = ['id']
        depth = 1

    def create(self, validated_data):
        self.date_created = timezone.now()
        self.save()
        return Account(**validated_data)