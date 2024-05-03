FROM  python:3.12.3-alpine3.19

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONBUFFERED=1
ENV SECRET_KEY=&$7t7nr_q38o15hpg&!+qa2%d7@&^6@@s10b8&_(t*ti)(dq@f

RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt


COPY . .
