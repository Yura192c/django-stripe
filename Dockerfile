FROM python:3.11.5

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PIP_ROOT_USER_ACTION=ignore


RUN pip install --upgrade pip

COPY Pipfile Pipfile.lock /solutionfactory-test-task/
RUN pip install pipenv && pipenv install --system

COPY . /app/


RUN python manage.py collectstatic --no-input


COPY . .

