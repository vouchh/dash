from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from rest_framework.schemas import get_schema_view

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'articles', views.ArticleViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]