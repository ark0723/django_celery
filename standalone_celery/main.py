from celery import Celery


"""
# celery app 생성 방법 1
app = Celery('worker',
             broker = 'redis://redis:6379/0',
             backend = 'redis://redis:6379/0',
             include = ['worker.tasks'])
"""
# celery app 생성 방법 2
app = Celery("worker", include=["worker.tasks"])
app.config_from_object("celeryconfig")

if __name__ == "__main__":
    app.start()
