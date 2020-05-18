from rest_framework import serializers
from .models import Article
from django.contrib.auth.models import User


class ArticleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = ['id','title', 'content', 'date_posted', 'author']

        #how to design request
        def create(self, validated_data):
            return Article(**validated_data)

