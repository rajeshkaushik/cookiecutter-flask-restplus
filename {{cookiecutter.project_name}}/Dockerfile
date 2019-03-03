FROM python:3.7.0-slim-stretch

WORKDIR /app

COPY Pipfile Pipfile.lock ./

RUN apt-get update \
  && apt-get install -y --no-install-recommends gcc libssl-dev libcurl4-openssl-dev \
  && pip install pipenv \
  && pipenv install --dev --system

ADD . /app
EXPOSE 8350
ENTRYPOINT ["gunicorn", "-c", "gunicorn_config.py", "wsgi:app"]
