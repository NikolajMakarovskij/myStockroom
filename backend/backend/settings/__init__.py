import os


DEBUG = int(os.environ.get("DEBUG", 1))

if DEBUG:
    from .production import *  # noqa 403
else:
    from .deploy import *  # noqa 403
