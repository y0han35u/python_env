FROM python:latest

WORKDIR /usr/src/atcoder

RUN apt update && apt install -y vim

