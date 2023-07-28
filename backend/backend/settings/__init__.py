import os


DEBUG = int(os.environ.get("DEBUG"))

if DEBUG:
    from .production import *
else:
    from .deploy import *


