# syntax=docker/dockerfile:1
FROM python:3
ENV PYTHONUNBUFFERED=1
RUN mkdir /api
COPY requirements.txt /api/
COPY manage.py /api/
COPY planeador_eventos_api /api/
WORKDIR /api
RUN pip install -r requirements.txt
