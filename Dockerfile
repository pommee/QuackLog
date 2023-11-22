FROM python:3.12.0

COPY . .

ADD main.py main.py

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000:8000

ENTRYPOINT [ "python", "main.py" ]