FROM python:3.11.9-slim-bullseye

RUN mkdir /crested_myna
WORKDIR /crested_myna

RUN apt-get update \
    && apt-get install -y postgresql-client --no-install-recommends \
        postgresql-client \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip
COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt
RUN pip install gunicorn

COPY ./.env.prod /crested_myna
COPY ./crested_myna /crested_myna