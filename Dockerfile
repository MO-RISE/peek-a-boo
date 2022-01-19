FROM python:3.9-slim

RUN apt-get update && apt-get install --no-install-recommends -y ffmpeg && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip3 install --no-cache-dir --upgrade -r requirements.txt

COPY main.py main.py

EXPOSE 80

# CMD ["/bin/sh"]
CMD ["python3", "main.py"]