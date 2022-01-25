FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip3 install --no-cache-dir --upgrade -r requirements.txt

COPY main.py main.py
COPY index.html index.html
COPY client.js client.js

EXPOSE 8000

ENTRYPOINT ["python3", "main.py", "--port", "8000"]