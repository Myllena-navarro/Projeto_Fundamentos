FROM python:3.11-slim

WORKDIR /app

COPY init_db.py /app/
COPY read_db.py /app/

CMD ["python", "read_db.py"]
