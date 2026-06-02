FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN mkdir -p logs

EXPOSE 8000

CMD ["uvicorn", "app.support_triage_engin_service:app", "--host", "0.0.0.0", "--port", "8000","--workers", "2"]