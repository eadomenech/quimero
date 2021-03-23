FROM python:3.8-slim-buster

WORKDIR /src

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
COPY . /src

CMD ["gunicorn", "-b", "127.0.0.1:8002", "application:create_app('config.ProductionConfig')"]
