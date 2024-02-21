FROM python:3.11.8-alpine3.19

WORKDIR /k8sdashboard

COPY requirements.txt requirements.txt

RUN python -m pip install --upgrade pip

RUN \
    apk update && \
    apk add build-base && \
    apk add gcc python3-dev musl-dev libffi-dev && \
    python -m pip install -r requirements.txt && \
    python -m pip install gunicorn cryptography

COPY app app

COPY migrations migrations

ADD table.py /k8sdashboard
ADD config.py /k8sdashboard 
ADD boot.sh /k8sdashboard

RUN chmod +x boot.sh

ENV FLASK_APP table.py

EXPOSE 5000
ENTRYPOINT ["/k8sdashboard/boot.sh"]
