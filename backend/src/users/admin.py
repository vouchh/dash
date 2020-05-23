from django.contrib import admin
from .models import Profile, Badge, Team, Signature, Agent, Role

admin.site.register(Profile)
admin.site.register(Badge)
admin.site.register(Team)
admin.site.register(Signature)
admin.site.register(Agent)
admin.site.register(Role)

