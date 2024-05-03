from celery import Celery


app = Celery("celery_worker")
app.config_from_object("celeryconfig")

app.conf.imports = ("cworker.tasks",)

app.autodiscover_tasks()