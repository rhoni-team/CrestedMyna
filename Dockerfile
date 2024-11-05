FROM python:3.11.9-slim-bullseye

RUN mkdir /crested_myna
WORKDIR /crested_myna

# Install postgres and GDAL
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
       gdal-bin libgdal-dev postgresql-client \
    && rm -rf /var/lib/apt/lists/*

# Set GDAL environment variable
ENV GDAL_LIBRARY_PATH=/usr/lib/libgdal.so

# Install python dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt
RUN pip install gunicorn

COPY ./.env.prod /crested_myna
COPY ./crested_myna /crested_myna