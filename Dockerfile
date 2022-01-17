FROM python:3

WORKDIR /app

COPY . /app

RUN mv geckodriver /usr/local/bin/geckodriver
RUN cd snapper && pip install -r requirements.txt
RUN cd src/
RUN export FLASK_APP=middleware.py
RUN export FLASK_ENV=production
RUN export path="$(pwd):$PATH"