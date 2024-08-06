import os

from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")

app = Celery("backend")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()
app.conf.timezone = "Asia/Yekaterinburg"


@app.task(bind=True)
def debug_task(self):
    """_debug_task_ Debug celery

    Args:
        self: _description_
        
    Returns:
        self.request: _description_
    """
    print("Request: {0!r}".format(self.request))
