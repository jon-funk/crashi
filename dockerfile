FROM python:3.9.1 as runtime
RUN mkdir -p /app
WORKDIR /app

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5005