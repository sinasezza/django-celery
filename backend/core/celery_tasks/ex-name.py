from core.celery_config import app


@app.task(queue='tasks')
def my_task():
    return