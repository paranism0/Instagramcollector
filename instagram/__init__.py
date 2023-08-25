from .client import Client
from .compatpatch import ClientCompatPatch
from .errors import (
    ClientLoginError, ClientLoginRequiredError
)
from .instagram_tasks import handleInstagram
__version__ = '1.6.0'
