from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
import uuid
from accounts import site_settings
from accounts.models import Account


class IntegrationType(models.Model):

    name = models.CharField(max_length=100)
    description = models.TextField()
    website = models.URLField(null=True, blank=True)
    icon = models.ImageField(null=True, blank=True)
    is_channel = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Integration(models.Model):

    account = models.ForeignKey(Account, on_delete=models.CASCADE, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    type = models.ForeignKey(IntegrationType, on_delete=models.DO_NOTHING)
    icon = models.ImageField(blank=True)
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    date_created = models.DateTimeField(default=timezone.now)
    date_cancelled  = models.DateTimeField(null=True, blank=True)
    date_updated = models.DateTimeField(null=True,blank=True)

    def __str__(self):
        return self.type.name


class IntegrationChat(models.Model):

    integration = models.OneToOneField(Integration, on_delete=models.CASCADE)
    title = models.CharField(max_length=100) # shows on chat window
    intro_text_business_hours = models.CharField(max_length=1000)
    intro_text_off_hours = models.CharField(max_length=1000)
    use_image = models.BooleanField(default=True)
    use_logo = models.BooleanField(default=True)
    header_color = models.CharField(max_length=7, default= "#172a72")
    chat_color = models.CharField(max_length=7, default= "#172a72")
    javascript_snippet= models.TextField()
    date_created = models.DateTimeField(default=timezone.now)
    date_disabled = models.DateTimeField(null=True)

    def __str__(self):
        return self.title


class IntegrationFacebook(models.Model):

    integration = models.OneToOneField(Integration, on_delete=models.CASCADE)
    facebook_id = models.CharField(max_length=100)
    facebook_page_id = models.CharField(max_length=100)
    facebook_ads_id = models.CharField(max_length=100)
    instagram_id = models.CharField(max_length=100)
    instagram_ads_id = models.CharField(max_length=100)
    messenger = models.BooleanField(default=True)
    enable_instagram_comments = models.BooleanField(default=True)
    enable_fb_posts_comments = models.BooleanField(default=True)
    enable_instagram_ads = models.BooleanField(default=True)
    import_history = models.BooleanField(default=True)
    token = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    messenger_code = models.TextField()
    date_created = models.DateTimeField(default=timezone.now)
    date_disabled = models.DateTimeField(null=True)

    def __str__(self):
        return self.facebook_id


class IntegrationEmail(models.Model):

    integration = models.OneToOneField(Integration, on_delete=models.CASCADE)
    email_address = models.EmailField()
    is_gmail_integration = models.BooleanField(default=True)
    is_outlook_integration = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    internal_email = models.CharField(max_length=100, unique=True)
    leave_mail_on_server = models.BooleanField(default=True)
    date_created = models.DateTimeField(default=timezone.now)
    date_disabled = models.DateTimeField(null=True)

    def __str__(self):
        return self.email_address

    #create a unique email for the integration where cusomer will forward their email
    def create(self):
        string = uuid.uuid4().hex[:8].lower()
        email = string+"@"+site_settings.DOMAIN
        self.internal_email = email
        self.save()