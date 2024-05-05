from core.celery_config import app
from celery import Task
import logging


logging.basicConfig(
    filename="app.log",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


class CustomTask(Task):
    def on_failure(self, exc, task_id, args, kwargs, einfo):
        # return super().on_failure(exc, task_id, args, kwargs, einfo)
        if isinstance(exc, ConnectionError):
            logging.error("connection error occurred.....")
        else:
            print(f"{task_id!r} failed: {exc!r}")
            
app.Task = CustomTask




@app.task(queue="tasks")
def my_task():
    try:
        raise ConnectionError("Connection error Occurred...")
    except ConnectionError as err:
        logging.error("connection error occurred.....")
        raise ConnectionError("Connection error occurred.....")



