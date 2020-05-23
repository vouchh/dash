from rest_framework import serializers
from .models import Ticket, Note, Message, Tag, CannedResponse
from accounts import helpers
from django.contrib.auth.models import User
from django.utils import timezone


class TicketSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ticket
        fields = ['id', 'subject', 'status', 'assigned_to_user',
                        'assigned_to_team', 'created_by', 'by_agent','has_priority',
                        'is_spam', 'tags', 'notes','integration', 'messages']
        read_only_fields = ['id']
        depth = 1

    def create(self, validated_data):
        self.date_created = timezone.now()
        self.save()
        return Ticket(**validated_data)


    def validate_request(self, request):
        if request.by_agent == True:
            user = User.objects.get(id=request.created_by)

            if user.profile.is_agent == True:
                return True
            return False


    def get_created_by(self, request):
        if request.created_by_user_id:
            user = User.objects.get(id==request.created_by_user_id)
            return user
        """
        If user id is not provided create a new user.    
        """
        if request.channel == 'email':
            email = request.address

            if not helpers.is_email(email):
                return False #throw exception here

            check_user = User.objects.filter(email==email)
            if not check_user:
                user = User(email = email)
                user.save()
                return user

            return check_user.first()
        return None


class MessageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Message
        fields = ['id', 'subject', 'body_html', 'body_text', 'account', 'send_status',
                  'by_agent', 'created_through', 'mail_headers', 'sent_by', 'sent_to', 'rule_id',
                  'canned_response_used','signature_used', 'external_id', 'to_address','from_address',
                  'sender_ip', 'date_created', 'date_opened']

        read_only_fields = ['id']
        depth = 1


class NoteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Note
        fields = ['id','status', 'content', 'ticket', 'date_created']

        read_only_fields = ['id']
        depth = 1


class CannedResponseSerializer(serializers.ModelSerializer):

    class Meta:
        model = CannedResponse
        fields = ['id','account', 'name', 'created_by', 'is_available_to_all', 'subject', 'body',
                  'attachments', 'tags']
        read_only_fields = ['id']
        depth = 1


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id','account', 'name']
        read_only_fields = ['id']
        depth = 1