FROM python:3.9-alpine

ENV PYTHONUNBUDERED 1

COPY ./requirements.txt /requirements.txt

run python -m pip install --upgrade pip
run pip install -r /requirements.txt

RUN mkdir /src
WORKDIR /src
COPY ./src /src

RUN adduser -D user
USER user