from rest_framework import serializers
from .models import Account
from django.utils import timezone


class AccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = Account
        fields = ['id', 'status', 'company_name', 'email', 'phone',
                  'domain', 'date_created', 'owner',]
        read_only_fields = ['id']
        depth = 1

    def create(self, validated_data):
        self.date_created = timezone.now()
        self.save()
        return Account(**validated_data)