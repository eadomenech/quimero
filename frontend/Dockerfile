FROM python:3.8-slim-buster

WORKDIR /src

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
COPY . /src

EXPOSE 8000

CMD ["gunicorn", "-b", "0.0.0.0:8000", "application:create_app('config.ProductionConfig')"]
