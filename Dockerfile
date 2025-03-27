FROM --platform=linux/amd64 python:3.13-slim

WORKDIR /app

RUN useradd -m -u 1000 appuser

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

COPY src /app/src
RUN mkdir -p /app/data/processed /app/data/interim

COPY data/processed/ /app/data/processed/
COPY data/interim/ /app/data/interim/

RUN chown -R appuser:appuser /app

USER appuser

EXPOSE 8501
EXPOSE 80

CMD ["streamlit", "run", "src/main.py", "--server.port=8501", "--server.address=0.0.0.0"]
