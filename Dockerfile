FROM python:3.7.7-slim
RUN pip install pipenv

WORKDIR /mqtt/
COPY Pipfile /mqtt/Pipfile
COPY Pipfile.lock /mqtt/Pipfile.lock
RUN pipenv install
COPY ./mqtt/ /mqtt/

CMD ["pipenv", "run", "python3", "app.py"]
