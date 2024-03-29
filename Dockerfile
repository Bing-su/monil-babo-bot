FROM python:3.10-slim

ENV TZ="Asia/Seoul"

WORKDIR /app

COPY pyproject.toml poetry.lock /app/

RUN pip install micropipenv[toml] && \
    micropipenv install && \
    pip cache purge

COPY . .

CMD ["python", "-O", "main.py"]
