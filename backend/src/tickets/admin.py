from django.contrib import admin
from .models import Ticket, Message, Note, Tag, AddressInfo, CannedResponse, Attachment

admin.site.register(Ticket)
admin.site.register(Message)
admin.site.register(Tag)
admin.site.register(Note)
admin.site.register(AddressInfo)
admin.site.register(CannedResponse)
admin.site.register(Attachment)
