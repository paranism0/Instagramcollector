
try:
    import urllib.error as compat_urllib_error
except ImportError:
    pass

try:
    import urllib.parse as compat_urllib_parse
except ImportError:
    pass

try:
    from urllib.parse import urlparse as compat_urllib_parse_urlparse
except ImportError:
    pass

try:
    import http.cookiejar as compat_cookiejar
except ImportError:
    pass

try:
    import pickle as compat_pickle
except ImportError:
    pass