import unittest
from flaskr.auth0.authManagementAPI import *
from flaskr import create_app
from flaskr.auth0 import auth0LoginMachine
from flaskr.auth0.auth import get_user_info
from flaskr.db.models import Visit, VitalSign, db
from flaskr.db import config


class ApplicationSimulation:
    """This class simulates the patient-visit-model endpoints"""

    def __init__(self, access_token):
        """Define variables and initialize test app context."""
        self.app = create_app(config.configs['test'])
        self.ctx = self.app.app_context()
        self.ctx.push()

        db.create_all()

        self.client = self.app.test_client
        self.access_token = access_token

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

    def create_visit(self, nurse_id, patient_id):
        """
        DESCRIPTION: Simulates creating a new visit record
        INPUT: nurse_id [string]: AUTH0 nurse id
               patient_id [string]: AUTH0 patient id
        OUTPUT: data [dictionary]: response from query with new data or error
        """
        query = '/visits/create'
        header = {"Authorization": f"Bearer {self.access_token}"}
        payload = {"nurse_id": nurse_id,
                   "patient_id": patient_id}

        server_response = self.client().post(query,
                                             headers=header,
                                             json=payload)
        data = server_response.get_json()

        return data

    def update_visit(self, visit_id, nurse_id=None, patient_id=None):
        """
        DESCRIPTION: Simulates updating an existing visit record
        INPUT: visit_id [integer]: Visit unique
                     primary ID key of the Visit Table
               nurse_id [string, OPTIONAL]: AUTH0 nurse user id
               patient_id [string, OPTIONAL]: AUTH0 patient user id
        OUTPUT: data [dictionary]: response from query
                      with update data or error
        """
        query = f'/visits/{visit_id}'
        header = {"Authorization": f"Bearer {self.access_token}"}

        if (nurse_id is not None) & (patient_id is not None):
            payload = {"nurse_id": nurse_id,
                       "patient_id": patient_id}
        elif (nurse_id is None) & (patient_id is not None):
            payload = {"patient_id": patient_id}
        elif (nurse_id is not None) & (patient_id is None):
            payload = {"nurse_id": nurse_id}
        else:
            payload = {}

        server_response = self.client().patch(query,
                                              headers=header,
                                              json=payload)
        data = server_response.get_json()

        return data

    def delete_visit(self, visit_id):
        """
        DESCRIPTION: Simulates deleting an
                     existing visit record
        INPUT: visit_id [integer]: Visit unique primary
                                   ID key of the Visit Table
        OUTPUT: data [dictionary]: response from query
                                   with deleted id or error
        """
        query = f'/visits/{visit_id}'
        header = {"Authorization": f"Bearer {self.access_token}"}

        server_response = self.client().delete(query,
                                               headers=header)
        data = server_response.get_json()

        return data

    def create_vitalsign(self, visit_id, tempCelsius):
        """
        DESCRIPTION: Simulates creating a new vital sign record
        INPUT: visit_id [integer]: Visit ID record
               tempCelsius [integer]: Patient temperature ( C )
        OUTPUT: data [dictionary]: response from query
                                   with new vital sign or error
        """
        query = '/vital-signs/create'
        header = {"Authorization": f"Bearer {self.access_token}"}
        payload = {"visit_id": visit_id,
                   "tempCelsius": tempCelsius}

        server_response = self.client().post(query,
                                             headers=header,
                                             json=payload)
        data = server_response.get_json()

        return data

    def update_vitalsign(self, vitalsign_id, visit_id=None, tempCelsius=None):
        """
        DESCRIPTION: Simulates updating an existing vital sign record
        INPUT: vitalsign_id [integer]: Vital Sign ID record
               visit_id [integer, OPTIONAL]:  Visit ID record
               tempCelsius [integer, OPTIONAL]:  new patient temperature ( C )

        OUTPUT: data [dictionary]: response from query
                                with updated vital sign or error
        """
        query = f'/vital-signs/{vitalsign_id}'
        header = {"Authorization": f"Bearer {self.access_token}"}

        if (visit_id is not None) & (tempCelsius is not None):
            payload = {"visit_id": visit_id,
                       "tempCelsius": tempCelsius}
        elif (visit_id is None) & (tempCelsius is not None):
            payload = {"tempCelsius": tempCelsius}
        elif (visit_id is not None) & (tempCelsius is None):
            payload = {"visit_id": visit_id}
        else:
            payload = {}

        server_response = self.client().patch(query,
                                              headers=header,
                                              json=payload)
        data = server_response.get_json()

        return data

    def delete_vitalsign(self, vitalsign_id):
        """
        DESCRIPTION: Simulates deleting an existing vital sign record
        INPUT: vitalsign_id [integer]: Vital Sign unique
                                primary ID key of the VitalSign Table
        OUTPUT: data [dictionary]: response from
                                    query with deleted id or error
        """
        query = f'/vital-signs/{vitalsign_id}'
        header = {"Authorization": f"Bearer {self.access_token}"}

        server_response = self.client().delete(query,
                                               headers=header)
        data = server_response.get_json()

        return data

    def search_patient_data(self, patient_id):
        """
        DESCRIPTION: Simulates searching patient medical data
                     from visit and vital sign records
        INPUT: patient_id [integer]: Patient AUTH0 ID
        OUTPUT: data [dictionary]: response from
                                query with patient data or error
        """
        query = f'/patients/search'
        header = {"Authorization": f"Bearer {self.access_token}"}
        payload = {"patient_id":  patient_id}

        server_response = self.client().get(query,
                                            headers=header,
                                            json=payload)

        data = server_response.get_json()

        return data

    def get_patient_user_data(self):
        """
        DESCRIPTION: Simulates active user patient
                     wanting to read their medical data
                     from visit and vital sign records
        INPUT: NONE
        OUTPUT: data [dictionary]: response from query
                                   with patient data or error
        """
        query = f'/patients/search/user'
        header = {"Authorization": f"Bearer {self.access_token}"}

        server_response = self.client().get(query,
                                            headers=header)
        data = server_response.get_json()

        return data


class StpRunner(unittest.TestCase):
    """This class runs the STP tests"""

    def setUp(self):
        """Define test variables"""
        # AUTH0 registered user credentials
        self.ADMIN_EMAIL = os.environ.get('ADMIN_EMAIL', None)
        self.NURSE_1_EMAIL = os.environ.get('NURSE_1_EMAIL', None)
        self.NURSE_2_EMAIL = os.environ.get('NURSE_2_EMAIL', None)
        self.PATIENT_1_EMAIL = os.environ.get('PATIENT_1_EMAIL', None)
        self.PATIENT_2_EMAIL = os.environ.get('PATIENT_2_EMAIL', None)
        self.USERS_PASSWORD = os.environ.get('USERS_PASSWORD', None)

        builder = Auth0ManagementAPIBuilder()
        self.auth0api = builder.load_base_url(). \
            load_access_token(). \
            load_users(). \
            load_roles(). \
            build()

        self.simulate_with_non_user = ApplicationSimulation.\
            Factory.\
            not_login_to_app()

        self.simulate_with_admin_user = ApplicationSimulation. \
            Factory. \
            login_to_app(self.ADMIN_EMAIL, self.USERS_PASSWORD)

        self.simulate_with_nurse_user = ApplicationSimulation. \
            Factory. \
            login_to_app(self.NURSE_1_EMAIL, self.USERS_PASSWORD)

        self.simulate_with_patient_user = ApplicationSimulation. \
            Factory. \
            login_to_app(self.PATIENT_1_EMAIL, self.USERS_PASSWORD)

    def tearDown(self):
        """Executed after reach test"""
        pass

    def STP_XX(self):
        """Quick, feel good, sanity check
           (no authorization needed)"""
        result = self.simulate_with_non_user.index()
        self.assertEqual(result['success'], True)

    def STP_01(self):
        """Test software with valid Admin Permissions """

        # get a list of nurse users
        role = self.auth0api.lut_role(['Nurse'])
        nurses = self.auth0api.filter_users_by_role(role)
        nurse = nurses[0]

        # get a list of patient users
        role = self.auth0api.lut_role(['Patient'])
        patients = self.auth0api.filter_users_by_role(role)
        patient = patients[0]

        result_visit = self.simulate_with_admin_user.\
            create_visit(nurse, patient)
        self.assertEqual(result_visit['success'], True)

        result_visit = self.simulate_with_admin_user.\
            update_visit(result_visit['data'].get('id'),
                         patient_id=patient)
        self.assertEqual(result_visit['success'], True)

        patientTemp = '44'
        result_vital = self.simulate_with_admin_user.\
            create_vitalsign(result_visit['data'].get('id'),
                             patientTemp)
        self.assertEqual(result_vital['success'], True)

        patientTemp = '55'
        result_vital = self.simulate_with_admin_user.\
            update_vitalsign(result_vital['data'].get('id'),
                             tempCelsius=patientTemp)
        self.assertEqual(result_vital['success'], True)

        result = self.simulate_with_admin_user.\
            search_patient_data(result_visit['data'].get('patient_id'))
        self.assertEqual(result['success'], True)

        result = self.simulate_with_admin_user.\
            delete_vitalsign(result_vital['data'].get('id'))
        self.assertEqual(result['success'], True)

        result = self.simulate_with_admin_user.\
            delete_visit(result_visit['data'].get('id'))
        self.assertEqual(result['success'], True)

    def STP_01_a(self):
        """Test software with unvalid Admin Permissions """
        result = self.simulate_with_admin_user.\
            get_patient_user_data()
        self.assertEqual(result['code'], 'unauthorized')
        self.assertEqual(result['description'],  'Permission not found.')

    def STP_02(self):
        """Test software with valid Nurse Permissions """
        # get a list of nurse users
        role = self.auth0api.lut_role(['Nurse'])
        nurses = self.auth0api.filter_users_by_role(role)
        nurse = nurses[0]

        # get a list of patient users
        role = self.auth0api.lut_role(['Patient'])
        patients = self.auth0api.filter_users_by_role(role)
        patient = patients[0]

        result_visit = self.simulate_with_nurse_user. \
            create_visit(nurse, patient)
        self.assertEqual(result_visit['success'], True)

        result_visit = self.simulate_with_nurse_user. \
            update_visit(result_visit['data'].get('id'),
                         patient_id=patient)
        self.assertEqual(result_visit['success'], True)

        patientTemp = '44'
        result_vital = self.simulate_with_nurse_user. \
            create_vitalsign(result_visit['data'].get('id'), patientTemp)
        self.assertEqual(result_vital['success'], True)

        patientTemp = '55'
        result_vital = self.simulate_with_nurse_user. \
            update_vitalsign(result_vital['data'].get('id'),
                             tempCelsius=patientTemp)
        self.assertEqual(result_vital['success'], True)

        result = self.simulate_with_nurse_user. \
            search_patient_data(result_visit['data'].get('patient_id'))
        self.assertEqual(result['success'], True)

    def STP_03(self):
        """Test software with unvalid Nurse Permissions """
        result = self.simulate_with_admin_user.\
            get_patient_user_data()
        self.assertEqual(result['code'], 'unauthorized')
        self.assertEqual(result['description'], 'Permission not found.')

        result = self.simulate_with_nurse_user. \
            delete_vitalsign('1')
        self.assertEqual(result['code'], 'unauthorized')
        self.assertEqual(result['description'], 'Permission not found.')

        result = self.simulate_with_nurse_user. \
            delete_visit('1')
        self.assertEqual(result['code'], 'unauthorized')
        self.assertEqual(result['description'], 'Permission not found.')

    def STP_04(self):
        """Test software with valid Patient Permissions """
        result = self.simulate_with_patient_user.\
            get_patient_user_data()
        self.assertEqual(result['success'], True)

    def STP_05(self):
        """Test software with unvalid Patient Permissions """
        result = self.simulate_with_patient_user. \
            create_visit('99999', '99999')
        self.assertEqual(result['code'], 'unauthorized')
        self.assertEqual(result['description'], 'Permission not found.')

        result = self.simulate_with_patient_user. \
            update_visit('99999', patient_id='99999')
        self.assertEqual(result['code'], 'unauthorized')
        self.assertEqual(result['description'], 'Permission not found.')

        patientTemp = '44'
        result = self.simulate_with_patient_user. \
            create_vitalsign('99999', patientTemp)
        self.assertEqual(result['code'], 'unauthorized')
        self.assertEqual(result['description'], 'Permission not found.')

        patientTemp = '55'
        result = self.simulate_with_patient_user. \
            update_vitalsign('99999', tempCelsius=patientTemp)
        self.assertEqual(result['code'], 'unauthorized')
        self.assertEqual(result['description'], 'Permission not found.')

        result = self.simulate_with_patient_user. \
            search_patient_data('999999')
        self.assertEqual(result['code'], 'unauthorized')
        self.assertEqual(result['description'], 'Permission not found.')

        result = self.simulate_with_patient_user. \
            delete_vitalsign('9999')
        self.assertEqual(result['code'], 'unauthorized')
        self.assertEqual(result['description'], 'Permission not found.')

        result = self.simulate_with_patient_user. \
            delete_visit('999999')
        self.assertEqual(result['code'], 'unauthorized')
        self.assertEqual(result['description'], 'Permission not found.')

    def STP_06(self):
        """Test software creates visit record"""
        # get a list of nurse users
        role = self.auth0api.lut_role(['Nurse'])
        nurses = self.auth0api.filter_users_by_role(role)
        nurse = nurses[0]

        # get a list of patient users
        role = self.auth0api.lut_role(['Patient'])
        patients = self.auth0api.filter_users_by_role(role)
        patient = patients[0]

        result = self.simulate_with_admin_user.create_visit(nurse, patient)

        self.assertEqual(result['success'], True)
        self.assertEqual(result['data'].get('patient_id'), patient)

    def STP_07(self):
        """Test software asserts during create visit record"""
        # get a list of nurse users
        role = self.auth0api.lut_role(['Nurse'])
        nurses = self.auth0api.filter_users_by_role(role)
        nurse = nurses[0]

        patient = '999999'
        result = self.simulate_with_admin_user.create_visit(nurse, patient)

        self.assertEqual(result['success'], False)
        self.assertEqual(result['error'], 422)

    def STP_08(self):
        """Test software updates visit record"""
        # get a list of patient users
        role = self.auth0api.lut_role(['Patient'])
        patients_list = self.auth0api.filter_users_by_role(role)

        # get last record in Visit
        visit = Visit.query.order_by(Visit.id.desc()).first()

        # pick a different patient that is not the visit record queried
        patients_filtered_list = list(filter(lambda x: x != visit.patient_id,
                                             patients_list))
        patient = patients_filtered_list[0]

        result = self.simulate_with_admin_user.update_visit(visit.id,
                                                            patient_id=patient)

        self.assertEqual(result['success'], True)
        self.assertEqual(result['data'].get('patient_id'), patient)

    def STP_09(self):
        """Test software asserts during patch visit record"""
        visit_id = '99999'
        patient = '999999'
        result = self.simulate_with_admin_user.update_visit(visit_id, patient)
        self.assertEqual(result['success'], False)
        self.assertEqual(result['error'], 422)

    def STP_10(self):
        """Test software deletes visit record"""
        # get list of visits
        visits = Visit.query.all()

        # find a visit record that has patient vital sign missing/incomplete
        visists_filtered = list(filter(
            lambda element: len(element.vitalsigns) == 0,
            visits))

        if len(visists_filtered) == 0:
            # list is empty : all visit records have vital signs records
            # create a new visit record with an existing patient
            print('Warning: All visit records have vital signs.'
                  'Cannot delete existing visit record. '
                  'Creating new visit record for test')
            tmp_visit = Visit.query.order_by(Visit.id.desc()).first()
            tmp_result = self.simulate_with_admin_user.\
                create_visit(tmp_visit.nurse_id, tmp_visit.patient_id)
            visists_filtered.append(Visit.
                                    query.
                                    get(tmp_result['data'].get('id')))

        # get one visit record for test
        visit = visists_filtered[0]

        result = self.simulate_with_admin_user.delete_visit(visit.id)

        self.assertEqual(result['success'], True)
        self.assertEqual(result['visit_id'], visit.id)

    def STP_11(self):
        """"Test software asserts during deletes visit record"""
        visit_id = '99999'
        result = self.simulate_with_admin_user.delete_visit(visit_id)

        self.assertEqual(result['success'], False)
        self.assertEqual(result['error'], 422)

    def STP_12(self):
        """Test software creates vital sign record"""
        # get list of visits
        visits = Visit.query.all()

        # find a visit record that has patient vital sign missing/incomplete
        visists_filtered = list(filter(
            lambda element: len(element.vitalsigns) == 0,
            visits))

        if len(visists_filtered) == 0:
            # list is empty : all visit records have vital signs records
            # create a new visit record with an existing patient
            print('Warning: All visit records have vital signs.'
                  ' Creating new visit record for test')
            tmp_visit = Visit.query.order_by(Visit.id.desc()).first()
            tmp_result = self.simulate_with_admin_user.\
                create_visit(tmp_visit.nurse_id, tmp_visit.patient_id)
            visists_filtered.append(Visit.
                                    query.
                                    get(tmp_result['data'].get('id')))

        # get one visit record for test
        visit = visists_filtered[0]

        # patient temperature
        tempCelsius = 37

        result = self.simulate_with_admin_user.\
            create_vitalsign(visit.id, tempCelsius)

        self.assertEqual(result['success'], True)
        self.assertEqual(result['data'].get('tempCelsius'), tempCelsius)

    def STP_13(self):
        """Test software asserts during creates vital sign record"""
        visit_id = 999999
        tempCelsius = 37
        result = self.simulate_with_admin_user.\
            create_vitalsign(visit_id, tempCelsius)

        self.assertEqual(result['success'], False)
        self.assertEqual(result['error'], 422)

    def STP_14(self):
        """Test software updates vital sign record"""
        # get last record in VitalSign
        vitalsign = VitalSign.query.order_by(VitalSign.id.desc()).first()
        tempCelsius = vitalsign.tempCelsius + 1

        result = self.simulate_with_admin_user.\
            update_vitalsign(vitalsign.id, tempCelsius=tempCelsius)

        self.assertEqual(result['success'], True)
        self.assertEqual(result['data'].get('tempCelsius'), tempCelsius)

    def STP_15(self):
        """Test software asserts during updates vital sign record"""
        # get VitalSigns
        vitalsign = VitalSign.query.all()

        vitalSignOne = vitalsign[0]
        vitalSignTwo = vitalsign[1]

        # it is not allowed to have one visit with two vital signs records
        # It questions which vital sign is the valid one.
        # Try to update vital sign record such that
        # two vital signs are from the same visit
        result = self.simulate_with_admin_user.\
            update_vitalsign(vitalSignOne.id, visit_id=vitalSignTwo.visit_id)

        self.assertEqual(result['success'], False)
        self.assertEqual(result['error'], 422)

    def STP_16(self):
        """Test software deletes vital sign record"""

        # get a vital sign record
        vitalsign = VitalSign.query.\
            order_by(VitalSign.id.desc()).first()

        result = self.simulate_with_admin_user.\
            delete_vitalsign(vitalsign.id)

        self.assertEqual(result['success'], True)
        self.assertEqual(result['vitalsign_id'], vitalsign.id)

    def STP_17(self):
        """"Test software asserts during deletes vital sign record"""
        vitalsign_id = '99999'

        result = self.simulate_with_admin_user.\
            delete_vitalsign(vitalsign_id)

        self.assertEqual(result['success'], False)
        self.assertEqual(result['error'], 422)

    def STP_18(self):
        """Test software can search for patient medical records"""
        # get a list of patient users
        role = self.auth0api.lut_role(['Patient'])
        patients_list = self.auth0api.filter_users_by_role(role)
        patient_id = patients_list[0]

        result = self.simulate_with_admin_user.\
            search_patient_data(patient_id)

        # verify success
        self.assertEqual(result['success'], True)

        # verify correct patient was queried
        for patient in result['data']:
            visit = patient.get('visit')
            self.assertEqual(visit['patient_id'], patient_id)

    def STP_19(self):
        """Test software asserts during a search for
           patient medical records"""
        patient_id = '999999'

        result = self.simulate_with_admin_user.\
            search_patient_data(patient_id)

        # verify success
        self.assertEqual(result['success'], False)
        self.assertEqual(result['error'], 404)

    def STP_20(self):
        """Test software can get patient medical records
           of the active patient user
           NOTE: Testing whether assertion for getting
                 active patient user profile
                 is tested with STPs that test user permissions"""
        result = self.simulate_with_patient_user.get_patient_user_data()

        auth0PatientInfo = get_user_info(self.
                                         simulate_with_patient_user.
                                         access_token)
        patient_id_expected = auth0PatientInfo.get('sub')

        # verify success
        self.assertEqual(result['success'], True)

        # verify active patient user was queried
        for patient in result['data']:
            visit = patient.get('visit')
            self.assertEqual(visit['patient_id'], patient_id_expected)


if __name__ == "__main__":
    suite = unittest.TestSuite()

    suite.addTest(StpRunner('STP_XX'))
    suite.addTest(StpRunner('STP_01'))
    suite.addTest(StpRunner('STP_01_a'))
    suite.addTest(StpRunner('STP_02'))
    suite.addTest(StpRunner('STP_03'))
    suite.addTest(StpRunner('STP_04'))
    suite.addTest(StpRunner('STP_05'))
    suite.addTest(StpRunner('STP_06'))
    suite.addTest(StpRunner('STP_07'))
    suite.addTest(StpRunner('STP_08'))
    suite.addTest(StpRunner('STP_09'))
    suite.addTest(StpRunner('STP_10'))
    suite.addTest(StpRunner('STP_11'))
    suite.addTest(StpRunner('STP_12'))
    suite.addTest(StpRunner('STP_13'))
    suite.addTest(StpRunner('STP_14'))
    suite.addTest(StpRunner('STP_15'))
    suite.addTest(StpRunner('STP_16'))
    suite.addTest(StpRunner('STP_17'))
    suite.addTest(StpRunner('STP_18'))
    suite.addTest(StpRunner('STP_19'))
    suite.addTest(StpRunner('STP_20'))

    unittest.TextTestRunner().run(suite)
