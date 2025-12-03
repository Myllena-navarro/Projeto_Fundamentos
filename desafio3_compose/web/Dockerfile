FROM python:3.11-slim

WORKDIR /app

COPY app.py .

RUN pip install flask psycopg2-binary redis

EXPOSE 5000

CMD ["python", "app.py"]
