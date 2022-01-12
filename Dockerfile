FROM python:3

WORKDIR /app

COPY . /app

RUN mv geckodriver /usr/local/bin/geckodriver
RUN cd snapper && pip install -r requirements.txt

