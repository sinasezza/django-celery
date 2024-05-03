import os
from celery import Celery


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")

app = Celery(main="core", broker=os.environ.get("CELERY_BROKER_URL"))
app.config_from_object("django.conf:settings", namespace="CELERY")

# app.conf.task_routes = {
#     'cworker.tasks.*': {'queue': 'queue1'},
#     'cworker.tasks.task2': {'queue': 'queue2'},
# }

app.conf.broker_transport_options = {
    'priority_steps': list(range(10)),
    'sep': ':',
    'queue_order_strategy': 'priority',
}

app.autodiscover_tasks()
