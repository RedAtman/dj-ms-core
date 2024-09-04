FROM python:3.10-alpine AS python-deps

COPY requirements_admin.txt /
COPY requirements.txt /

RUN apk add --no-cache py3-virtualenv py3-pip git && \
    python3 -m venv /.venv && \
    source /.venv/bin/activate && \
    pip install --upgrade pip && \
    pip install -r /requirements.txt --no-cache-dir


FROM python:3.10-alpine AS runtime

RUN apk add --no-cache git curl

ENV PATH="/.venv/bin:$PATH"

ENV PYTHONUNBUFFERED=1

WORKDIR /home/django

COPY --from=python-deps /.venv /.venv

ARG CACHE_DATE=not_a_date
RUN echo $CACHE_DATE

ADD . .

ENTRYPOINT ["/home/django/entrypoint.sh"]

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

EXPOSE 8000
