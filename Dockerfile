FROM python:3.11-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV YTHONUNBUFFERED 1

COPY requirements.txt temp/requirements.txt
COPY src /src

WORKDIR src

RUN pip install -r /temp/requirements.txt