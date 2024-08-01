import os


DEBUG = int(1)#(os.environ.get("DEBUG")) # type: ignore[arg-type]

if DEBUG:
    from .production import *  # noqa F403
else:
    from .deploy import *  # noqa F403
