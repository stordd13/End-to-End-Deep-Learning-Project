FROM python:3.8-slim-buster

RUN apt-get update -y && apt-get install -y build-essential awscli
WORKDIR /app

COPY . /app
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD ["python3", "app.py"]