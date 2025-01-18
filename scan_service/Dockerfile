FROM python:3.8-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY app.py /app/
COPY aws_services /app/aws_services

EXPOSE 5001

CMD ["python", "app.py"]
