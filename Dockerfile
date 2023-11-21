FROM python:3.12.0-slim

WORKDIR /app

ADD main.py main.py

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD [ "python", "./main.py" ]