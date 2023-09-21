FROM  tiangolo/uwsgi-nginx-flask:latest
WORKDIR /app/
COPY main.py .
