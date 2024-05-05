import os
import time
from celery import Celery
from kombu import Queue, Exchange


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")

app = Celery(main="core")
app.config_from_object("django.conf:settings", namespace="CELERY")


app.conf.task_queues = [
    Queue(
        name='tasks', 
        exchange=Exchange('tasks'), 
        routing_key='tasks',
        queue_arguments={'x-max-priority': 10}  
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
task_dir = os.path.join(base_dir, 'core', 'celery_tasks')

if os.path.exists(task_dir) and os.path.isdir(task_dir):
    task_modules = []
    for filename in os.listdir(task_dir):
        if filename.startswith('ex') and filename.endswith('.py'):
            module_name = f"core.celery_tasks.{filename[:-3]}"
            
            module = __import__(module_name, fromlist=['*'])

            for name in dir(module):
                obj = getattr(module, name)
                if callable(obj):
                    task_modules.append(f"{module_name}.{name}")

    app.autodiscover_tasks(task_modules, related_name='tasks')

