# pull official base image
FROM python:3.11-rc-bullseye
# set work directory
WORKDIR /myBase
# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
# install psycopg2 dependencies
RUN apt-get update \
    && apt-get install -y postgresql-server-dev-all gcc python3-dev musl-dev
# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip3 install -r requirements.txt

# copy project
COPY . .
