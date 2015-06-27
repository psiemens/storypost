import requests
import json

class APIResource(object):

	def __init__(self, api):
		self.callable = False
		self.api = api

	def __call__(self):
		self.callable = True
		return self

	def __str__(self):
		if hasattr(self, 'data') and self.data:
			return self.data
		else:
			return self._get().__str__()

	def __iter__(self):
		return self._list().__iter__()

	def __getitem__(self, key):
  		return self._list()[key]

class ListMember(APIResource):
	def __init__(self, api, list_id=None, id=None, data=None):
		super(ListMember, self).__init__(api)
		self.list_id = list_id
		self.id = id
		self.data = data

	def _get(self):
		r = self.api.get('lists/' + self.list_id + '/members/' + self.id)
		return r.json()

	def delete(self):
		r = self.api.delete('lists/' + self.list_id + '/members/' + self.id)
		return r.status_code == 204

class ListMembers(APIResource):

	def __init__(self, api, id=None):
		super(ListMembers, self).__init__(api)
		self.id = id

	def _get(self):
		return self._list()

	def _list(self):
		r = self.api.get('lists/' + self.id + '/members/')
		response = r.json()
		return response['members']

	def add(self, email):
		payload = {
			'email_address': email,
			'status': 'subscribed'
		}
		r = self.api.post('lists/' + self.id + '/members/', payload=payload)
		data = r.json()
		return ListMember(self.api, list_id=self.id, id=data['id'], data=data)

	def get(self, id):
		return ListMember(self.api, list_id=self.id, id=id)

class Lists(APIResource):

    def get(self, id):
        def _get():
            r = self.api.get('lists/' + id)
            return r.json()
        self.id = id
        self._get = _get
        return self

    def _get(self):
        r = self.api.get('lists/')
        json = r.json()
        return json['lists']

    def _list(self):
        return self._get()

    def add(self, name, contact, permission_reminder, use_archive_bar, campaign_defaults, email_type_option=False):
        payload = {
            'name': name,
            'contact': contact,
            'permission_reminder': permission_reminder,
            'use_archive_bar': use_archive_bar,
            'campaign_defaults': campaign_defaults,
            'email_type_option': email_type_option
        }
        r = self.api.post('lists', payload=payload)
        return r.json()


    @property
    def members(self):
        return ListMembers(self.api, self.id)


class Campaign(APIResource):

	def __init__(self, api, id=None, data=None):
		super(Campaign, self).__init__(api)
		self.id = id

	def _get(self):
		r = self.api.get('campaigns/' + self.id)
		return r.json()

	def _list(self):
		return self._get()

	def send(self):
		payload = {
			'apikey': self.api.api_key,
			'cid': self.id
		}
		r = self.api.get('campaigns/send/', payload=payload, auth=False, version='2.0')
        data = r.json()
		return 'complete' in data and data['complete']:

class Campaigns(APIResource):

	def _get(self):
		r = self.api.get('campaigns/')
		json = r.json()
		return json['campaigns']

	def _list(self):
		return self._get()

	def get(self, id):
		return Campaign(self.api, id=id)

	def create(self, type='regular', options=None, content=None, from_email=None, from_name=None, to_name=None):
		payload = {
			'apikey': self.api.api_key,
			'type': type,
			'options': options,
			'content': content,
			'from_email': from_email,
			'from_name': from_name,
			'to_name': to_name,
		}
		r = self.api.post('campaigns/create/', payload=payload, auth=False, version='2.0')
		return r.json()


class MailChimp(object):

	API_DEFAULT_VERSION = '3.0'
	API_BASE = 'https://%s.api.mailchimp.com/%s/'

	def __init__(self, api_username, api_key, version=API_DEFAULT_VERSION):
		self.api_username = api_username
		self.api_key = api_key
		self.version = version
		self.datacenter = self.get_datacenter(api_key)

	def get_datacenter(self, api_key):
		pieces = api_key.split('-')
		try:
			return pieces[1]
		except:
			print 'INVALID API KEY'

	def get_base_url(self, version=None):
		if version is None: 
			version = self.version
		return self.API_BASE % (self.datacenter, version)

	def get_auth(self):
		return (self.api_username, self.api_key)

	def get(self, endpoint='', payload=None, auth=True, version=None):
		if auth:
			return requests.get(self.get_base_url(version) + endpoint, params=payload, auth=self.get_auth())
		else:
			return requests.get(self.get_base_url(version) + endpoint, params=payload)

	def post(self, endpoint='', payload=None, auth=True, version=None):
		if auth:
			return requests.post(self.get_base_url(version) + endpoint, data=json.dumps(payload), auth=self.get_auth())
		else:
			return requests.post(self.get_base_url(version) + endpoint, data=json.dumps(payload))

	def delete(self, endpoint='', auth=True, version=None):
		if auth:
			return requests.delete(self.get_base_url(version) + endpoint, auth=self.get_auth())
		else:
			return requests.delete(self.get_base_url(version) + endpoint)

	def test(self):
		r = self.get('')
		print r.json()['contact']['city']

	@property
	def lists(self):
		return Lists(self)

	@property
	def campaigns(self):
		return Campaigns(self)
