import unittest
from flaskr import create_app

from urllib.request import urlopen, Request
from urllib import parse
import os
import json

AUTH0_DOMAIN = os.environ.get('AUTH0_DOMAIN', None)
AUTH0_AUDIENCE = os.environ.get('AUTH0_AUDIENCE', None)
AUTH0_SCOPE = os.environ.get('AUTH0_SCOPE', None)
AUTH0_CLIENT_ID = os.environ.get('AUTH0_CLIENT_ID', None)
AUTH0_CLIENT_SECRET = os.environ.get('AUTH0_CLIENT_SECRET', None)

def get_user_token():
    url = 'https://{}/oauth/token'.format(AUTH0_DOMAIN)

    data2 = {'grant_type': 'password',
            'username=': 'admin@nursevisitmodel.com',
            'password': 'Alvaro123',
            'audience': AUTH0_AUDIENCE,
            'scope': AUTH0_SCOPE,
            'client_id': AUTH0_CLIENT_ID,
            'client_secret': AUTH0_CLIENT_SECRET}


    header = 'content-type: application/x-www-form-urlencoded'
    data = f'grant_type=password&username=admin@nursevisitmodel.com&password=Alvaro123&audience={AUTH0_AUDIENCE}&scope={AUTH0_SCOPE}&client_id={AUTH0_CLIENT_ID}&client_secret={AUTH0_CLIENT_SECRET}'


    datacurl = f'curl --request POST --url {url} --header {header} --data {data}'


    datacurl = 'curl --request POST --url \'{}\' --header \'{}\' --data \'{}\' '.format( url, header, data)

    print(datacurl)

   # data_parse = parse.urlencode(data2).encode()

  #  req = Request(url,
  #                headers={'content-type': 'application/x-www-form-urlencoded'},
   #               data=data_parse)


 #   respond = urlopen(req)
  #  data = respond.read()

    return True


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

        tempdata = get_user_token()

        print(tempdata)

        self.assertEqual(data['success'], True)


if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(PatientVisitTestCase('STP_01'))
    unittest.TextTestRunner().run(suite)
