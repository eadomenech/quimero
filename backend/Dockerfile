FROM python:3.8-slim-buster

RUN pip install fastapi uvicorn

COPY ./app /app

CMD ["uvicorn", "app.main:app", "--host", "127.0.0.1", "--port", "8001"]

