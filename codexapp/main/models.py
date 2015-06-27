from django.conf import settings
from django.db.models import Model, IntegerField, CharField, TextField, ForeignKey, OneToOneField
from codexapp.remote import mailchimp


class User(Model):

    auth_user = OneToOneField(settings.AUTH_USER_MODEL)

    name = CharField(max_length=255)


class List(Model):

    user = ForeignKey(User)
    mc_list_id = CharField(max_length=255) # Mapped to MailChmip List instance
    title = CharField(max_length=255)
    description = TextField()

    @property
    def members(self):
        return mailchimp.lists.get(self.mc_list_id).members()

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):

        if not self.pk:

            contact = {
                "company": 'test company',
                "address1": 'test address 1',
                "city": 'san francisco',
                "state": 'california',
                "zip": '97213',
                "country": 'United States'
            }

            campaign_defaults = {
                "from_name": 'Peter Siemens',
                "from_email": 'peterjsiemens@gmail.com',
                "subject": "test list 123",
                "language": 'english'
            }

            mc_list = mailchimp.lists.add(name=self.title, contact=contact, permission_reminder='test reminder', use_archive_bar=False, campaign_defaults=campaign_defaults)

            self.mc_list_id = mc_list['id']

        super(List, self).save(*args, **kwargs)


class Prompt(Model):

    user = ForeignKey(User)
    mc_campaign_id = CharField(max_length=255) # Mapped to MailChmip Campaign instance
    message = TextField()
    description = TextField()
    list = ForeignKey(List)

    def save(self, *args, **kwargs):

        if not self.pk:

            options = {
                'list_id': self.list.mc_list_id,
                'subject': self.message,
                'from_email': 'peterjsiemens@gmail.com',
                'from_name': 'Peter Siemens',
                'to_name': 'Test people'
            }

            content = {
                'html': 'This is a test email',
                'text': 'This is a test email'
            }

            campaign = mailchimp.campaigns.create(options=options, content=content, from_email='peterjsiemens@gmail.com', from_name='Peter Siemens', to_name='John Smith')

            self.mc_campaign_id = campaign['id']

        super(Prompt, self).save(*args, **kwargs)
