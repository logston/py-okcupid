import requests
import json
import time


class Client:
    def __init__(self):
        self.session =  None

    def login(self, username, password):
        self.session = requests.Session()

        data = {
            'username': username,
            'password': password,
            'okc_api': 1,
        }

        self.session.post('https://www.okcupid.com/login', data=data)

    def search(self):

        search_params = {
            'after': None,
            'age_recip': 'on',
            'answers': [],
            'availability': 'any',
            'cats': [],
            'children': [],
            'dogs': [],
            'drinking': [],
            'drugs': [],
            'education': [],
            'ethnicity': [],
            #'fields': 'userinfo,thumbs,percentages,likes,last_contacts,online',
            'fields': 'userinfo',
            'gender_tags': None,
            'gentation': [34],
            'i_want': 'women',
            'interest_ids': [],
            'languages': 0,
            'last_login': 2678400,
            'limit': 18,
            'located_anywhere': 0,
            'location': None,
            'locid': None,
            'looking_for': [],
            'lquery': '',
            'maximum_age': 46,
            'maximum_height': None,
            'minimum_age': 22,
            'minimum_height': None,
            'monogamy': 'unknown',
            'order_by': 'SPECIAL_BLEND',
            'orientation_tags': None,
            'radius': 25,
            'religion': [],
            'smoking': [],
            'speaks_my_language': 0,
            'tagOrder': ['speaks_my_language'],
            'they_want': 'men'
        }

        return SearchResult(self.session, search_params)

    def profile(self, username):
        url = 'https://www.okcupid.com/profile/{}'.format(username)
        resp = self.session.get(url)
        return resp.content


class SearchResult:
    url = 'https://www.okcupid.com/1/apitun/match/search'

    def __init__(self, session, search_params):
        self.session = session
        self.search_params = search_params
        self.cached_results = []

    def __iter__(self):
        return self

    def __next__(self):
        resp = self.session.post(self.url, json=self.search_params)
        content = json.loads(resp.content.decode())
        return content['data']

