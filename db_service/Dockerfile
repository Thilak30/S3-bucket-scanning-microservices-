FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

COPY ./my.cnf /etc/mysql/my.cnf

EXPOSE 5002

CMD ["python", "app.py"]
