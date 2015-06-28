from django.conf import settings

from mailchimp import MailChimp

def mailchimp(api_key):
    return MailChimp('codex', api_key)
