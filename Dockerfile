FROM python:3.7
ENV PYTHONUNBUFFERED 1
WORKDIR /srv
COPY requirements.txt /srv/
RUN pip install --no-cache-dir -r requirements.txt

