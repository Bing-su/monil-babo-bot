FROM python:3.9-slim

RUN apt update && apt install -y gcc git

WORKDIR /app

COPY pyproject.toml poetry.lock /app/

RUN pip install --no-cache-dir poetry && \
    poetry config virtualenvs.create false && \
    poetry install --no-dev

COPY . .

CMD ["python", "-OO", "main.py"]