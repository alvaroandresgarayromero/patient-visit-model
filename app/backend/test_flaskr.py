import unittest
import os
import requests
from flaskr.auth0.authManagementAPI import *
from flaskr import create_app


AUTH0_DOMAIN = os.environ.get('AUTH0_DOMAIN', None)
AUTH0_AUDIENCE = os.environ.get('AUTH0_AUDIENCE', None)
AUTH0_SCOPE = os.environ.get('AUTH0_SCOPE', None)
AUTH0_CLIENT_ID = os.environ.get('AUTH0_CLIENT_ID', None)
AUTH0_CLIENT_SECRET = os.environ.get('AUTH0_CLIENT_SECRET', None)

AUTH0_MANAGEMENT_AUDIENCE = os.environ.get('AUTH0_MANAGEMENT_AUDIENCE', None)
AUTH0_MANAGEMENT_CLIENT_ID = os.environ.get('AUTH0_MANAGEMENT_CLIENT_ID', None)
AUTH0_MANAGEMENT_CLIENT_SECRET = os.environ.get('AUTH0_MANAGEMENT_CLIENT_SECRET', None)

ADMIN_EMAIL = os.environ.get('ADMIN_EMAIL', None)
USERS_PASSWORD = os.environ.get('USERS_PASSWORD', None)

'''
INPUT: 
    a_username [string]: email of AUTH0 user
    a_password [string]: password of AUTH0 user
    
OUTPUT:
    respond [dict] : token information in dictionary format 
                     where 'access_token' key is the JWT token.
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


class PatientVisitTestCase(unittest.TestCase):
    """This class represents the patient-visit-model test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client

    def tearDown(self):
        """Executed after reach test"""
        pass

    def STP_01(self):
        query = '/'
        server_response = self.client().get(query)
        data = server_response.get_json()

        self.assertEqual(data['success'], True)


if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(PatientVisitTestCase('STP_01'))
    unittest.TextTestRunner().run(suite)
