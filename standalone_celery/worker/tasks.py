from main import app

# 주의점: django의 celery와 celery standalone의 함수가 동일해야함
# 예: django celery: add, dumb 있고 celery-standalone: add, mul, xsum이 있음
# dumb.delay() 적용했을 경우, django celery가 할당됐다면 문제가 없으나,
# celery-standalone이 할당되면 keyerror발생


@app.task
def add(x, y):
    return x + y


@app.task
def mul(x, y):
    return x * y


@app.task
def xsum(numbers):
    return sum(numbers)
