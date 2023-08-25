
class Constants(object):
    """Constants holder class that stores the bulk of the fixed strings used in the library."""

    IG_SIG_KEY = '19ce5f445dbfd9d29c59dc2a78c616a7fc090a8e018b9267bc4240a30244c53b'
    IG_CAPABILITIES = '3brTvw=='
    SIG_KEY_VERSION = '4'
    APP_VERSION = '76.0.0.15.395'
    APPLICATION_ID = '567067343352427'
    FB_HTTP_ENGINE = 'Liger'

    ANDROID_VERSION = 24
    ANDROID_RELEASE = '7.0'
    PHONE_MANUFACTURER = 'samsung'
    PHONE_DEVICE = 'SM-G930F'
    PHONE_MODEL = 'herolte'
    PHONE_DPI = '640dpi'
    PHONE_RESOLUTION = '1440x2560'
    PHONE_CHIPSET = 'samsungexynos8890'
    VERSION_CODE = '138226743'

    USER_AGENT_FORMAT = \
        'Instagram {app_version} Android ({android_version:d}/{android_release}; ' \
        '{dpi}; {resolution}; {brand}; {device}; {model}; {chipset}; en_US; {version_code})'

    USER_AGENT_EXPRESSION = \
        r'Instagram\s(?P<app_version>[^\s]+)\sAndroid\s\((?P<android_version>[0-9]+)/(?P<android_release>[0-9\.]+);\s' \
        r'(?P<dpi>\d+dpi);\s(?P<resolution>\d+x\d+);\s(?P<manufacturer>[^;]+);\s(?P<device>[^;]+);\s' \
        r'(?P<model>[^;]+);\s(?P<chipset>[^;]+);\s[a-z]+_[A-Z]+;\s(?P<version_code>\d+)'

    USER_AGENT = USER_AGENT_FORMAT.format(**{
        'app_version': APP_VERSION,
        'android_version': ANDROID_VERSION,
        'android_release': ANDROID_RELEASE,
        'brand': PHONE_MANUFACTURER,
        'device': PHONE_DEVICE,
        'model': PHONE_MODEL,
        'dpi': PHONE_DPI,
        'resolution': PHONE_RESOLUTION,
        'chipset': PHONE_CHIPSET,
        'version_code': VERSION_CODE})