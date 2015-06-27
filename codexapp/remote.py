from django.conf import settings

from mailchimp import MailChimp

mailchimp = MailChimp(settings.MC_API_USERNAME, settings.MC_API_KEY)
