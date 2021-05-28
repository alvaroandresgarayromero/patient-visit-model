import requests
import os

AUTH0_DOMAIN = os.environ.get('AUTH0_DOMAIN', None)
AUTH0_AUDIENCE = os.environ.get('AUTH0_AUDIENCE', None)
AUTH0_SCOPE = os.environ.get('AUTH0_SCOPE', None)
AUTH0_CLIENT_ID = os.environ.get('AUTH0_CLIENT_ID', None)
AUTH0_CLIENT_SECRET = os.environ.get('AUTH0_CLIENT_SECRET', None)


'''
Login and retrieve AUTH0 user JWT token

INUPUT:
    a_username [string]: Email of user
    a_password [string]: Password of user
OUTPUT:
    access_token [string]: JWT token of user

NOTE: User must be registered (in the database) of AUTH0
NOTE: To see registered users credentials, see auth0.env file.
NOTE: This function is useful for scripts that would
      like to automate the JWT retrieval for testing purposes
'''


def get_user_token(a_username, a_password):
    url = f'https://{AUTH0_DOMAIN}/oauth/token'

    header = {'content-type': 'application/x-www-form-urlencoded'}

    payload = {'grant_type': 'password',
               'username': a_username,
               'password': a_password,
               'audience': AUTH0_AUDIENCE,
               'scope': AUTH0_SCOPE,
               'client_id': AUTH0_CLIENT_ID,
               'client_secret': AUTH0_CLIENT_SECRET}

    respond = requests.post(url,
                            headers=header,
                            data=payload)
    oauth = respond.json()
    access_token = oauth.get('access_token')

    return access_token
