from django.db.models import Model, IntegerField, CharField, TextField
from codexapp.remote import mailchimp

class List(Model):

    mc_list_id = CharField(max_length=255) # Mapped to MailChmip List instance
    title = CharField(max_length=255)
    description = TextField()

    @property
    def members(self):
        return mailchimp.lists.get(self.mc_list_id).members()

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

    mc_campaign_id = CharField(max_length=255) # Mapped to MailChmip Campaign instance
    message = TextField()
    description = TextField()




