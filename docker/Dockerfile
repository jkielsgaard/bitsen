FROM ubuntu:20.04

RUN apt update
RUN apt-get install -y python3.9 python3-pip python3-dev build-essential gcc libsnmp-dev snmp-mibs-downloader

RUN pip3 install --upgrade pip

RUN mkdir /app
WORKDIR /app
COPY . /app
RUN pip3 install -r requirements.txt

WORKDIR /app/api
CMD python3 api.py

WORKDIR /app/engine
CMD python3 engine.py