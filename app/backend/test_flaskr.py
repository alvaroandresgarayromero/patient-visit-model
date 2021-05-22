import unittest
from flaskr.auth0.authManagementAPI import *
from flaskr import create_app
from flaskr.auth0 import auth0LoginMachine
from flaskr.db.models import setup_db

# create a test database in the same postgres container
user = os.environ.get('POSTGRES_USER_APP', None)
password = os.environ.get('POSTGRES_PASSWORD_APP', None)
host = os.environ.get('POSTGRES_CONTAINER_NAME_APP', None)
database = os.environ.get('POSTGRES_DB_APP', None)
port = os.environ.get('POSTGRES_PORT_TEST', None)

# AUTH0 registered user credentials
ADMIN_EMAIL = os.environ.get('ADMIN_EMAIL', None)
NURSE_EMAIL = os.environ.get('NURSE_EMAIL', None)
PATIENT_1_EMAIL = os.environ.get('PATIENT_1_EMAIL', None)
PATIENT_2_EMAIL = os.environ.get('PATIENT_2_EMAIL', None)
USERS_PASSWORD = os.environ.get('USERS_PASSWORD', None)


class ApplicationSimulation:
    """This class simulates the patient-visit-model endpoints"""

    def __init__(self, access_token):
        """Define variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.access_token = access_token
        self.database_path = f'postgresql://{user}:{password}@{host}:{port}/{database}'

        setup_db(self.app, self.database_path)

    class Factory:
        @staticmethod
        def login_to_app(a_username, a_password):
            access_token = auth0LoginMachine.get_user_token(a_username,
                                                            a_password)
            return ApplicationSimulation(access_token)

        @staticmethod
        def not_login_to_app():
            return ApplicationSimulation(None)

    def index(self):
        query = '/'
        server_response = self.client().get(query)
        data = server_response.get_json()
        return data

    def create_visit(self, patient_id):
        query = '/visits/create'
        header = {"Authorization": f"Bearer {self.access_token}"}
        payload = {"patient_id": patient_id}

        server_response = self.client().post(query,
                                             headers=header,
                                             json=payload)
        data = server_response.get_json()

        return data

    def update_visit(self, patient_id):
        query = '/visits/create'
        header = {"Authorization": f"Bearer {self.access_token}"}
        payload = {"patient_id": patient_id}

        server_response = self.client().post(query,
                                             headers=header,
                                             json=payload)
        data = server_response.get_json()

        return data

    def delete_visit(self, patient_id):
        query = '/visits/create'
        header = {"Authorization": f"Bearer {self.access_token}"}
        payload = {"patient_id": patient_id}

        server_response = self.client().post(query,
                                             headers=header,
                                             json=payload)
        data = server_response.get_json()

        return data


class StpRunner(unittest.TestCase):
    """This class runs the STP tests"""

    def setUp(self):
        """Define test variables"""
        builder = Auth0ManagementAPIBuilder()
        self.auth0api = builder.load_base_url(). \
            load_access_token(). \
            load_users(). \
            load_roles(). \
            build()

    def tearDown(self):
        """Executed after reach test"""
        pass

    def STP_XX(self):
        """Quick feel good, sanity check ( no authorization needed)"""
        simulate = ApplicationSimulation.Factory.not_login_to_app()
        result = simulate.index()
        self.assertEqual(result['success'], True)

    def STP_06(self):
        """Test software creates visit record"""
        simulate = ApplicationSimulation.Factory.login_to_app(ADMIN_EMAIL, USERS_PASSWORD)

        # get a list of patient users
        role = self.auth0api.lut_role(['Patient'])
        patients = self.auth0api.filter_users_by_role(role)
        patient = patients[0]
        result = simulate.create_visit(patient)

        self.assertEqual(result['success'], True)
        self.assertEqual(result['data'].get('patient_id'), patient)

    def STP_07(self):
        """Test software creates visit record asserts with unknown parameter"""
        simulate = ApplicationSimulation.Factory.login_to_app(ADMIN_EMAIL, USERS_PASSWORD)

        patient = 'unknown_id'
        result = simulate.create_visit(patient)

        self.assertEqual(result['success'], False)
        self.assertEqual(result['error'], 422)



if __name__ == "__main__":
    suite = unittest.TestSuite()
   # suite.addTest(StpRunner('STP_XX'))
    suite.addTest(StpRunner('STP_06'))
   # suite.addTest(StpRunner('STP_07'))

    unittest.TextTestRunner().run(suite)
