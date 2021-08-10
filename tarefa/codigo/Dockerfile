FROM python:3.8-slim

COPY . /tarefa
COPY requirements .

RUN pip install -r requirements

WORKDIR /tarefa

CMD ["uvicorn", "main:app","--host", "0.0.0.0", "--port", "80", "--reload"]
