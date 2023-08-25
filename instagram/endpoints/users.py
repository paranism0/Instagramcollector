from ..compatpatch import ClientCompatPatch


class UsersEndpointsMixin(object):
    """For endpoints in ``/users/``."""

    def user_info(self, user_id):
        """
        Get user info for a specified user id

        :param user_id:
        :return:
        """
        res = self._call_api(endpoint = 'users/{user_id!s}/info/'.format(**{'user_id': user_id}) , method = "GET")
        if self.auto_patch:
            ClientCompatPatch.user(res['user'], drop_incompat_keys=self.drop_incompat_keys)
        return res

    def username_info(self, user_name):
        """
        Get user info for a specified user name
        :param user_name:
        :return:
        """
        res = self._call_api(endpoint = 'users/{user_name!s}/usernameinfo/'.format(**{'user_name': user_name}) , method = "GET")
        if self.auto_patch:
            ClientCompatPatch.user(res['user'], drop_incompat_keys=self.drop_incompat_keys)
        return res