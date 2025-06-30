from celery import Celery
import subprocess

app = Celery('tasks', broker='redis://redis:6379/0')

app.conf.update(
    broker_connection_retry_on_startup=True
)

@app.task(bind=True, max_retries=None)
def add(self, command):
    try:
        subprocess.check_output(command, shell=True)
    except Exception as e:
        self.retry(countdown=10)