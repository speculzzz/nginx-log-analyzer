FROM python:3.9-slim

WORKDIR /nginx_log_analyzer
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["uvicorn", "nginx_log_analyzer.main:app", "--host", "0.0.0.0", "--port", "80"]
