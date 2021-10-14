FROM python:3.7

RUN mkdir -p /opt/blask

COPY . /opt/blask

WORKDIR /opt/blask

RUN pip install pipenv
RUN pipenv install --python `which python` --dev
RUN pipenv install gunicorn --python `which python`

CMD pipenv run gunicorn -b 0.0.0.0:8000 --workers 2 main
