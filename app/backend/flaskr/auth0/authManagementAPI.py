import os
import requests
import numpy as np

'''
Example to how to build auth0 management API

# Use builder for piecewise construction
builder = Auth0ManagementAPIBuilder()
obj = builder.load_base_url(). \
    load_access_token(). \
    load_users(). \
    load_roles(). \
    build()

# get all users with Patient Role

# get the role as LUT
patient_role = obj.lut_role(['Patient'])

# get user ids with roles that match the requested role
patient_users_id = obj.filter_users_by_role(patient_role)

# optionally, get the user name
names = obj.get_user_name(patient_users_id)


'''

AUTH0_DOMAIN = os.\
    environ.\
    get('AUTH0_DOMAIN', None)
AUTH0_MANAGEMENT_AUDIENCE = os.\
    environ.\
    get('AUTH0_MANAGEMENT_AUDIENCE', None)
AUTH0_MANAGEMENT_CLIENT_ID = os.\
    environ.\
    get('AUTH0_MANAGEMENT_CLIENT_ID', None)
AUTH0_MANAGEMENT_CLIENT_SECRET = os.\
    environ.\
    get('AUTH0_MANAGEMENT_CLIENT_SECRET', None)


class Auth0ManagementAPI:
    def __init__(self):
        self.base_url = None
        self.access_token = None
        self.list_users = None
        self.list_roles = None

    '''
    Fetch the name of the user

    INTPUT:
        a_user_id [list] : A list of AUTH0 user ID elements of type string
    OUTPUT:
        user_name [list] : A list of user elements names of type string

    NOTE: This is not the username email
    '''

    def get_user_name(self, a_user_id):

        assert type(a_user_id) == list, 'Input data a_user_id must be a list'

        url_list = list(map(
            lambda user_id:
            f'{self.base_url}/api/v2/users/{user_id}?'
            f'fields=name&include_fields=true',
            a_user_id))

        bearer_token = f'Bearer {self.access_token}'
        header = {'Authorization': bearer_token}

        respond_list = list(map(lambda url:
                                requests.get(url, headers=header).json(),
                                url_list))

        user_namelist = list(map(lambda oauth:
                                 oauth.get('name'),
                                 respond_list))

        assert None not in user_namelist, 'A user id was not ' \
                                          'found in Auth0 database'

        return user_namelist

    '''
    Fetch the role of the user

    INTPUT:
        a_user_id [list] : A list of AUTH0 user ID elements of type string
    OUTPUT:
        respond_list [list] : A list with element dictionaries
             [ { 'id': '***', 'name': '***', 'description':'***'}, ...]
    '''

    def get_user_role(self, a_user_id):

        assert type(a_user_id) == list, 'Input data a_user_id must be a list'

        url_list = list(map(lambda user_id:
                            f'{self.base_url}/api/v2/users/'
                            f'{user_id}/roles',
                            a_user_id))

        bearer_token = f'Bearer {self.access_token}'
        header = {'Authorization': bearer_token}

        respond_list = list(map(lambda url:
                                requests.get(url, headers=header).json()[0],
                                url_list))

        return respond_list

    '''
    Fetches role info such as the id and description

    Supported Role Names: 'Admin', 'Patient', 'Nurse'

    INTPUT:
        a_role [list] : A list with one or more elements role
                        names to look up as string
    OUTPUT:
        result [list] :  A list with element dictionaries
          [ { 'id': '***', 'name': '***', 'description':'***'}, ...]
    '''

    def lut_role(self, a_role):

        assert type(a_role) == list, 'Input data a_role must be a list'

        lut_long = np.array(self.list_roles)

        lut = np.array(list(map(lambda element:
                                element.get('name'),
                                lut_long)))

        # masking the array
        logical_idx = lut == a_role[0]
        for role in a_role[1:]:
            logical_idx = np.logical_or(logical_idx, lut == role)

        return list(lut_long[logical_idx])

    '''
    Filter uses from 'list_users' element

    INTPUT:
        a_role [list] : A list of role of type dictionary.
                        ex see: obj.lut_role(['Patient'])
    OUTPUT:
        users [list] : A list of users with the requested role
    '''

    def filter_users_by_role(self, a_role):
        assert type(a_role) == list, 'Input data a_role must be a list'

        # list of all users
        users = np.array(self.list_users)

        # fetch each user role
        user_roles = np.array(self.get_user_role(self.list_users))

        logical_idx = user_roles == a_role[0]
        for role in a_role[1:]:
            logical_idx = np.logical_or(logical_idx, user_roles == role)

        return list(users[logical_idx])


class Auth0ManagementAPIBuilder:
    def __init__(self):
        self.root = Auth0ManagementAPI()

    def build(self):
        return self.root

    def load_base_url(self):
        self.root.base_url = f'https://{AUTH0_DOMAIN}'
        return self

    '''
    INTPUT:
        NONE
    OUTPUT:
        access_token [string] : AUTH0 Management API token
    '''

    # @todo: need to add support when the token expires
    def load_access_token(self):
        url = f'{self.root.base_url}/oauth/token'
        payload = {'grant_type': 'client_credentials',
                   'audience': AUTH0_MANAGEMENT_AUDIENCE,
                   'client_id': AUTH0_MANAGEMENT_CLIENT_ID,
                   'client_secret': AUTH0_MANAGEMENT_CLIENT_SECRET}

        respond = requests.post(url, data=payload)
        oauth = respond.json()
        self.root.access_token = oauth.get('access_token')
        return self

    '''
    INTPUT:
        NONE
    OUTPUT:
        user_ids [list] :  A list of users id's
                           where the ID elements are string
    '''

    def load_users(self):
        url = f'{self.root.base_url}/api/v2/users?' \
              f'fields=user_id&include_fields=true'

        bearer_token = f'Bearer {self.root.access_token}'
        header = {'Authorization': bearer_token}

        respond = requests.get(url, headers=header)
        oauth = respond.json()

        self.root.list_users = list(map(lambda element:
                                        element.get('user_id'),
                                        oauth))
        return self

    '''
    INTPUT:
        NONE
    OUTPUT:
        oauth [list] : A list of all roles with elements of type dictionary
       [{ 'id': '***', 'name': '***', 'description':'***'}, ... ]
    '''

    def load_roles(self):
        url = f'{self.root.base_url}/api/v2/roles'

        bearer_token = f'Bearer {self.root.access_token}'
        header = {'Authorization': bearer_token}

        respond = requests.get(url, headers=header)
        oauth = respond.json()
        self.root.list_roles = oauth
        return self
