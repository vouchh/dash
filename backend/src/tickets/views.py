from django.shortcuts import render
from rest_framework.decorators import api_view
from accounts import helpers
from tickets.models import Ticket, Message, Note, Tag, CannedResponse
from integrations.models import Integration, IntegrationType
from .serializers import TicketSerializer, MessageSerializer, NoteSerializer, TagSerializer, CannedResponseSerializer
from rest_framework.response import Response
from rest_framework import viewsets


@api_view(['GET'])
def home(request):

    IntegrationType.objects.all().delete()
    Integration.objects.all().delete()

    context = {
        'car': 'car'
    }
    return render(request, 'tickets/home.html', context)


@api_view(['POST'])
def set_ticket_status(request):
    request = helpers.clean_request(request)

    ticket_id = request['ticket_id']
    status = request['status']

    if ticket_id == "" or status == "":
        return Response({"data": "empty request"}, status=400)

    if helpers.set_ticket_status(ticket_id, status) == True:
        return Response({"data": "Status Change was Successful"}, status=200)

    return Response({"data": "Status Change was NOT Successful"}, status=400)

@api_view(['POST'])
def assign_ticket(request):
    request = helpers.clean_request(request)

    return Response({"data": "Status Change was NOT Successful"}, status=400)

@api_view(['POST'])
def set_ticket_priority(request):
    request = helpers.clean_request(request)

    return Response({"data": "Status Change was NOT Successful"}, status=400)

@api_view(['POST'])
def ticket_spam_status(request):
    request = helpers.clean_request(request)

    return Response({"data": "Status Change was NOT Successful"}, status=400)



class TicketViewSet(viewsets.ModelViewSet):

    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    permission_classes = []
    authentication_classes = []

class MessageViewSet(viewsets.ModelViewSet):

    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = []
    authentication_classes = []

class NoteViewSet(viewsets.ModelViewSet):

    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = []
    authentication_classes = []
    filter_fields = ['status', 'has_priority']

class TagViewSet(viewsets.ModelViewSet):

    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = []
    authentication_classes = []
    filter_fields = ['status', 'has_priority']


class CannedResponseViewSet(viewsets.ModelViewSet):

    queryset = CannedResponse.objects.all()
    serializer_class = CannedResponseSerializer
    permission_classes = []
    authentication_classes = []
    filter_fields = ['status', 'has_priority']
