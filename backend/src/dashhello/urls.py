from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls')),
    url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^rest-auth/registration/', include('rest_auth.registration.urls')),

    path('', include('tickets.urls')),
    path('', include('integrations.urls')),
    path('', include('accounts.urls')),
    path('', include('users.urls')),
    path('', include('articles.urls')),
]






