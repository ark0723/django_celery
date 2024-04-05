FROM python:3.11-alpine3.19

# ensures that the python output 
# i.e. the stdout and stderr streams are sent straight to terminal 
ENV PYTHONUNBUFFERED 1

ARG DEV=false

COPY requirements.txt /app/
COPY . /app/

WORKDIR /app
RUN pip install -r requirements.txt