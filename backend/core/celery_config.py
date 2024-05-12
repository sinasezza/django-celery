import os
import time

import sentry_sdk
from sentry_sdk.integrations.celery import CeleryIntegration
from celery import Celery
from kombu import Queue, Exchange
from django.conf import settings


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")

app: Celery = Celery(main="core")
app.config_from_object("django.conf:settings", namespace="CELERY")

### SENTRY CONFIG
sentry_dsn = os.environ.get("SENTRY_DSN")

print(f"sentry dsn is {sentry_dsn} \n\n\n")

sentry_sdk.init(
    dsn=sentry_dsn,
    integrations=[
        CeleryIntegration(),
    ],
)


app.conf.task_queues = [
    Queue(
        name="tasks",
        exchange=Exchange("tasks"),
        routing_key="tasks",
        queue_arguments={"x-max-priority": 10},
    ),
]


app.conf.task_acks_late = True
app.conf.task_default_priority = 5
app.conf.worker_prefetch_multiplier = 1
app.conf.worker_concurrency = 1


# app.conf.task_routes = {
#     'cworker.tasks.*': {'queue': 'queue1'},
#     'cworker.tasks.task2': {'queue': 'queue2'},
# }

# app.conf.task_default_rate_limit = '1/m'

# app.conf.broker_transport_options = {
#     'priority_steps': list(range(10)),
#     'sep': ':',
#     'queue_order_strategy': 'priority',
# }


base_dir = os.getcwd()

# Discover tasks in core/celery_tasks
task_modules = []
task_dir = os.path.join(base_dir, "core", "celery_tasks")
if os.path.exists(task_dir) and os.path.isdir(task_dir):
    for filename in os.listdir(task_dir):
        if filename.startswith("ex") and filename.endswith(".py"):
            module_name = f"core.celery_tasks.{filename[:-3]}"
            task_modules.append(module_name)

# Autodiscover tasks in installed apps (excluding core) and the discovered tasks in core/celery_tasks
app.autodiscover_tasks(
    lambda: [app_name for app_name in settings.INSTALLED_APPS] + task_modules,
    related_name="tasks",
)
