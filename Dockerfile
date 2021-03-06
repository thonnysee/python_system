FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN apt-get -y update && apt-get -y upgrade 
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY . /code/
RUN adduser --disabled-login dockuser
USER dockuser