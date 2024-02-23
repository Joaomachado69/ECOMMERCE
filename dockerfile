FROM python:3.11

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /code

RUN apt-get update && apt-get install -y netcat

COPY requirements.txt /code/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /code/



##docker build -t myproject .
##ocker run -it myproject bash