from .serializers import ArticleSerializer
from .models import Article
from rest_framework import viewsets, permissions
from rest_framework.decorators import api_view
from django.contrib.auth.models import User

#how to design response
class ArticleViewSet(viewsets.ModelViewSet):

    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
