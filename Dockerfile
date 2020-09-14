FROM python:3

ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY . /code

COPY wait-for-it.sh wait-for-it.sh
RUN chmod +x wait-for-it.sh

RUN pip install -r requirements.txt
