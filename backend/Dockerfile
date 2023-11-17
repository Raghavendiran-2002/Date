# syntax=docker/dockerfile:1.4
FROM --platform=$BUILDPLATFORM python:3.10-alpine AS builder

WORKDIR /code
COPY requirements.txt /code
RUN pip3 install -r requirements.txt

COPY . .

ENV FLASK_APP main.py
ENV FLASK_ENV development
ENV FLASK_RUN_PORT 3000
ENV FLASK_RUN_HOST 0.0.0.0

EXPOSE 3000

CMD ["flask", "run"]
