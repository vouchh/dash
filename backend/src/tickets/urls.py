from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'tickets', views.TicketViewSet)
router.register(r'tags', views.TagViewSet)
router.register(r'notes', views.NoteViewSet)
router.register(r'messages', views.MessageViewSet)
router.register(r'canned_responses', views.CannedResponseViewSet)


# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', views.home, name="home"),
    path('', include(router.urls)),
    path('set_ticket_status/', views.set_ticket_status, name='set_ticket_status'),
    path('assign_ticket/', views.assign_ticket, name='assign_ticket'),
    path('set_ticket_priority/', views.set_ticket_priority, name='set_ticket_priority'),
    path('ticket_spam_status/', views.ticket_spam_status, name='ticket_spam_status'),
]