import unittest
import os
import requests
from flaskr.auth0.authManagementAPI import *
from flaskr import create_app

ADMIN_EMAIL = os.environ.get('ADMIN_EMAIL', None)
USERS_PASSWORD = os.environ.get('USERS_PASSWORD', None)


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
