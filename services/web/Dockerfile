# pull official base image
FROM python:3.8.1-slim-buster

# set work directory
WORKDIR /Users/shawnachatfield/workspace/python-code-challenge/services/web

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install system dependencies
RUN apt-get update && apt-get install -y netcat

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /Users/shawnachatfield/workspace/python-code-challenge/services/web/requirements.txt
RUN pip install -r requirements.txt

# copy project
COPY . /Users/shawnachatfield/workspace/python-code-challenge/services/web


# run entrypoint.sh
ENTRYPOINT ["/Users/shawnachatfield/workspace/python-code-challenge/services/web/entrypoint.sh"]