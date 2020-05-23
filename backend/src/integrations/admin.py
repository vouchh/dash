from django.contrib import admin
from .models import Integration, IntegrationType, IntegrationChat, IntegrationEmail, IntegrationFacebook

admin.site.register(Integration)
admin.site.register(IntegrationType)
admin.site.register(IntegrationEmail)
admin.site.register(IntegrationChat)
admin.site.register(IntegrationFacebook)



