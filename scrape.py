import time

from okcupid import Client
from bs4 import BeautifulSoup
from random import random
import json
import os


def main():
    c = Client()

    username = os.environ.get('USERNAME')
    password = os.environ.get('PASSWORD')

    user_blobs = 'user_blobs.txt'
    profile_blob_dir = 'profiles'

    c.login(username, password)
    cursor = c.search()

    for record_set in cursor:
        for user in record_set:
            try:
                with open(user_blobs, 'a') as fp:
                    fp.write(json.dumps(user) + '\n')
                username = user.get('username')
                content = c.profile(username)
                soup = BeautifulSoup(content.decode(), 'html.parser')
                profile = soup.find(id='react-profile-essays')
                html = profile.prettify()
                with open('{}/{}'.format(profile_blob_dir, username), 'w') as fp:
                    fp.write(html)
                time.sleep(random())
            except Exception as e:
                print(e)

main()

