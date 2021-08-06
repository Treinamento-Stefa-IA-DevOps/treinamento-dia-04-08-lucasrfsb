FROM python:3.8-slim

RUN pip install pandas fastapi sklearn uvicorn[standart]

COPY . /app

ENV PYTHONPATH=/app

WORKDIR /app

CMD ["uvicorn", "codigo.main:app","--host", "0.0.0.0", "--port", "80", "--reload"]
