import os


DEBUG = int(os.environ.get("DEBUG", 1))

if DEBUG:
    from .production import *  # noqa F403
else:
    from .deploy import *  # noqa F403
