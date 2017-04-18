FROM python:2.7

RUN mkdir -p /usr/src/app
ONBUILD COPY . /usr/src/app

WORKDIR /usr/src/app
RUN pip install -r requirements.txt
ENTRYPOINT ["python", "App.py"]