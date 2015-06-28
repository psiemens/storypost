from django.conf import settings

from mailchimp import MailChimp

def mailchimp(api_key):
    return MailChimp(settings.MC_API_USERNAME, api_key)
