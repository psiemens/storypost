from datetime import datetime

from django.conf import settings
from django.db.models import Model, IntegerField, CharField, TextField, ForeignKey, OneToOneField, DateTimeField
from codexapp.remote import mailchimp

class User(Model):

    auth_user = OneToOneField(settings.AUTH_USER_MODEL)

    name = CharField(max_length=255)
    mc_api_key = CharField(max_length=255)

    date_joined = DateTimeField(auto_now_add=True)

    @property
    def email(self):
        return self.auth_user.email


class List(Model):

    user = ForeignKey(User)
    mc_list_id = CharField(max_length=255) # Mapped to MailChmip List instance
    title = CharField(max_length=255)
    description = TextField()

    @property
    def members(self):
        return mailchimp(self.user.mc_api_key).lists.get(self.mc_list_id).members()

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):

        if not self.pk:

            contact = {
                "company": 'Codex Hackathon',
                "address1": '111 Mission St.',
                "city": 'San Francisco',
                "state": 'California',
                "zip": '97213',
                "country": 'United States'
            }

            campaign_defaults = {
                "from_name": self.user.name,
                "from_email": self.user.email,
                "subject": self.title,
                "language": 'english'
            }

            permission_reminder = 'You are recieving this email because you subscribed to the %s list.' % self.title

            mc_list = mailchimp(self.user.mc_api_key).lists.add(name=self.title, contact=contact, permission_reminder=permission_reminder, use_archive_bar=False, campaign_defaults=campaign_defaults)

            self.mc_list_id = mc_list['id']

        super(List, self).save(*args, **kwargs)

    def add_member(self, user):
        try:
            mailchimp(self.user.mc_api_key).lists.get(self.mc_list_id).members.add(user.email)
        except:
            pass

    def remove_member(self, user):
        try:
            mailchimp(self.user.mc_api_key).lists.get(self.mc_list_id).members.remove(user.email)
        except:
            pass

class Reply(Model):

    prompt = ForeignKey('Prompt')
    mc_conversation_id = CharField(max_length=255, null=True, unique=True) # Mapped to MailChmip Conversation instance
    email = CharField(max_length=255)
    content = TextField()
    user = ForeignKey(User, null=True)
    timestamp = DateTimeField()

class Prompt(Model):

    user = ForeignKey(User)
    mc_campaign_id = CharField(max_length=255) # Mapped to MailChmip Campaign instance
    title = CharField(max_length=255)
    message = TextField()
    description = TextField()
    list = ForeignKey(List)

    @property
    def replies(self):
        return Reply.objects.filter(prompt=self)

    def send(self):
        return mailchimp(self.user.mc_api_key).campaigns.get(self.mc_campaign_id).send()

    def sync_replies(self):

        try:
            last_reply = Reply.objects.order('-timestamp')[0]
            last_timestamp = last_reply.timestamp
        except:
            last_timestamp = datetime.fromtimestamp(0)

        conversations = mailchimp(self.user.mc_api_key).campaigns.get(self.mc_campaign_id).conversations()

        replies = [c for c in conversations if datetime.strptime(c['last_message']['timestamp'], "%Y-%m-%d %H:%M:%S") > last_timestamp]

        for reply in replies:
            try:
                try:
                    user = User.objects.get(email=reply['last_message']['from_email'])
                except:
                    user = None
                reply_obj = Reply(prompt=self, mc_conversation_id=reply['id'], email=reply['last_message']['from_email'], content=reply['last_message']['message'], user=user, timestamp=datetime.strptime(reply['last_message']['timestamp'], "%Y-%m-%d %H:%M:%S"))
                reply_obj.save()
            except:
                reply_obj = Reply.objects.get(mc_conversation_id=reply['id'])
                reply_obj.content = reply['last_message']['message']
                reply_obj.timestamp = datetime.strptime(reply['last_message']['timestamp'], "%Y-%m-%d %H:%M:%S")
                reply_obj.save()


    def get_html(self):
        from django.template.loader import render_to_string
        return render_to_string('prompt/email.html', {'prompt': self})

    def save(self, *args, **kwargs):

        if not self.pk:

            to_name = self.list.title + ' subscribers'

            options = {
                'list_id': self.list.mc_list_id,
                'subject': self.title,
                'from_email': self.user.email,
                'from_name': self.user.name,
                'to_name': to_name
            }

            content = {
                'html': self.get_html(),
                'text': self.message,
            }

            campaign = mailchimp(self.user.mc_api_key).campaigns.create(options=options, content=content, from_email=self.user.email, from_name=self.user.name, to_name=to_name)

            self.mc_campaign_id = campaign['id']

        super(Prompt, self).save(*args, **kwargs)



