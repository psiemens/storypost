from mailchimp import MailChimp
from jinja2 import Environment, PackageLoader

API_USERNAME = 'psiemens'
API_KEY = '52e4e752068da129a885713f200740e8-us1'

m = MailChimp(API_USERNAME, API_KEY)

#print m.lists.get('d9fa19092f').members.add('peterjsiemens@gmail.com')
#for member in m.lists.get('d9fa19092f').members():
#	print member['email_address']

#print m.campaigns()[0]['id']
#print m.campaigns.get('8ebd35bfe6').send()
#for member in m.lists.get('d9fa19092f').members(): #add('peterjsiemens7@gmail.com').delete()
#	print member['email_address']

#m.test()

options = {
	'list_id': 'd9fa19092f',
	'subject': 'testing 2',
	'from_email': 'peterjsiemens@gmail.com',
	'from_name': 'Peter Siemens',
	'to_name': 'Test people'
}

content = {
	'html': 'This is a test email',
	'text': 'This is a test email'
}
#m.createCampaign(options=options, content=content, from_email='peterjsiemens@gmail.com', from_name='Peter Siemens', to_name='John Smith')

#env = Environment(loader=PackageLoader('codex', 'templates'))

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
print m.lists.add(name="Test list 123", contact=contact, permission_reminder='test reminder', use_archive_bar=False, campaign_defaults=campaign_defaults)