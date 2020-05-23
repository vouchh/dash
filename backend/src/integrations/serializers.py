from rest_framework import serializers
from .models import Integration
from django.utils import timezone


class IntegrationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Integration
        fields = ['id', 'account', 'type', 'icon', 'created_by', 'is_active', 'date_created']
        read_only_fields = ['id']
        depth = 1

    def create(self, validated_data):
        self.date_created = timezone.now()
        self.save()
        return Integration(**validated_data)