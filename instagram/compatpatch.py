# -*- coding: utf-8 -*-


class ClientCompatPatch(object):
    """Utility to make entities from the private api similar to the ones
    from the public one by adding the necessary properties, and if required,
    remove any incompatible properties (to save storage space for example).
    """

    @staticmethod
    def _drop_keys(obj, keys):
        """
        Drop unwanted dict keys

        :param obj:
        :param keys:
        :return:
        """
        for k in keys:
            obj.pop(k, None)

    @classmethod
    def user(cls, user, drop_incompat_keys=False):
        """Patch a user object """
        user['id'] = str(user['pk'])
        user['bio'] = user.get('biography', '')
        user['profile_picture'] = user['profile_pic_url']
        user['website'] = user.get('external_url', '')
        if 'media_count' in user and 'follower_count' in user and 'following_count' in user:
            counts = {
                'media': user['media_count'],
                'followed_by': user['follower_count'],
                'follows': user['following_count']
            }
            user['counts'] = counts
        if drop_incompat_keys:
            cls._drop_keys(
                user,
                [
                    'auto_expand_chaining',
                    'biography',
                    'external_lynx_url',
                    'external_url',
                    'follower_count',
                    'following_count',
                    'geo_media_count',
                    'has_anonymous_profile_picture',
                    'has_chaining',
                    'hd_profile_pic_url_info',
                    'hd_profile_pic_versions',
                    'include_direct_blacklist_status',
                    'is_business',
                    'is_favorite',
                    'is_private',
                    'is_unpublished',
                    'is_verified',
                    'media_count',
                    'pk',
                    'profile_context',
                    'profile_pic_id',
                    'profile_pic_url',
                    'usertags_count',
                ]
            )
        return user