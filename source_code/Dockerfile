FROM python:3
ENV PYTHONUNBUFFERED 1

# Change timezone to UTC+7

ENV TZ=Asia/Ho_Chi_Minh
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone


WORKDIR /usr/src/app
ADD requirements.txt /usr/src/app

RUN pip install -r requirements.txt
