import json
from ..errors import (
    ClientError, ClientLoginError
)
from ..compatpatch import ClientCompatPatch
try:
    ConnectionError = ConnectionError
except NameError:
    class ConnectionError(Exception):
        pass


class AccountsEndpointsMixin(object):
    """For endpoints in ``/accounts/``."""

    def login(self):
        """Login."""
        prelogin_params = self._call_api(
            endpoint = 'si/fetch_headers/',
            params='',
            query={'challenge_type': 'signup', 'guid': self.generate_uuid(True)},
            return_response=True)

        if not self.csrftoken:
            raise ClientError(
                'Unable to get csrf from prelogin.',
                error_response=prelogin_params.text)

        login_params = {
            'device_id': self.device_id,
            'guid': self.uuid,
            'adid': self.ad_id,
            'phone_id': self.phone_id,
            '_csrftoken': self.csrftoken,
            'username': self.username,
            'password': self.password,
            'login_attempt_count': '0',
        }

        login_response = self._call_api(
            endpoint = 'accounts/login/', params=login_params, return_response=True)

        if not self.csrftoken:
            raise ClientError(
                'Unable to get csrf from login.',
                error_response=login_response.text)

        login_json = json.loads(login_response)
        if not login_json.get('logged_in_user', {}).get('pk'):
            raise ClientLoginError('Unable to login.')

        if self.on_login:
            on_login_callback = self.on_login
            on_login_callback(self)

    def current_user(self):
        """Get current user info"""
        params = self.authenticated_params
        res = self._call_api(endpoint = 'accounts/current_user/', params=params, query={'edit': 'true'})
        if self.auto_patch:
            ClientCompatPatch.user(res['user'], drop_incompat_keys=self.drop_incompat_keys)
        return res

    def logout(self):
        """Logout user"""
        params = {
            'phone_id': self.phone_id,
            '_csrftoken': self.csrftoken,
            'guid': self.uuid,
            'device_id': self.device_id,
            '_uuid': self.uuid
        }
        return self._call_api(endpoint =  'accounts/logout/', params=params, unsigned=True)