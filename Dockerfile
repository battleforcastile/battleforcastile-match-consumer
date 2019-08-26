FROM python:3.7.0-slim

RUN pip3 install --no-cache-dir pipenv

RUN mkdir /app
WORKDIR /app

COPY Pipfile Pipfile
COPY Pipfile.lock Pipfile.lock

RUN pipenv install --deploy --system

COPY . /app

CMD python3 battleforcastile_match_consumer/run_consumer.py
