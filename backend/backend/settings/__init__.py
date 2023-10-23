import os


DEBUG = int(os.environ.get("DBG_BKND"))

if DEBUG:
    from .production import *
else:
    from .deploy import *


