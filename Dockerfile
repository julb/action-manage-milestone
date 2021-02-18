FROM python:3.9-slim AS builder
RUN mkdir /app
COPY main.py /app
COPY requirements.txt /app
WORKDIR /app
RUN pip install -r requirements.txt --target=/app

FROM python:3.9-slim
COPY --from=builder /app /app
WORKDIR /app
ENV PYTHONPATH /app
CMD ["python3", "/app/main.py"]