FROM python:3.11.3

LABEL org.opencontainers.image.authors="phooshmand@gmail.com"
LABEL version="1.0"

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get install 
RUN apt-get update && apt-get install -y \
    default-libmysqlclient-dev \
    build-essential \
    cron \
    && rm -rf /var/lib/apt/lists/*
RUN mkdir /app

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD ["gunicorn", "--workers=4", "Graveyard.wsgi", "--bind", "0.0.0.0:8000"]