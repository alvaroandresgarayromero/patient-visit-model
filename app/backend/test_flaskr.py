import unittest
from flaskr.auth0.authManagementAPI import *
from flaskr import create_app
from flaskr.auth0 import auth0LoginMachine

ADMIN_EMAIL = os.environ.get('ADMIN_EMAIL', None)
USERS_PASSWORD = os.environ.get('USERS_PASSWORD', None)


class PatientVisitTestCase(unittest.TestCase):
    """This class represents the patient-visit-model test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.access_token = auth0LoginMachine.get_user_token(ADMIN_EMAIL,
                                                             USERS_PASSWORD)

        builder = Auth0ManagementAPIBuilder()
        self.auth0api = builder.load_base_url(). \
            load_access_token(). \
            load_users(). \
            load_roles(). \
            build()

    def tearDown(self):
        """Executed after reach test"""
        pass

    '''
    Quick feel good, sanity check 
    '''
    def STP_01(self):
        query = '/'
        server_response = self.client().get(query)
        data = server_response.get_json()

        self.assertEqual(data['success'], True)

    def STP_02(self):
        query = '/visits/create'

        header = {"Authorization": f"Bearer {self.access_token}"}

        # get a list of registered patients
        role = self.auth0api.lut_role(['Patient'])
        patients = self.auth0api.filter_users_by_role(role)
        payload = {"patient_id": patients[1]}

        server_response = self.client().post(query,
                                             headers=header,
                                             json=payload)
        data = server_response.get_json()
        self.assertEqual(data['success'], True)


if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(PatientVisitTestCase('STP_01'))
    suite.addTest(PatientVisitTestCase('STP_02'))

    unittest.TextTestRunner().run(suite)
