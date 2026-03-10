FROM python:3.9

WORKDIR /app

COPY . .

CMD ["python", "log_analyzer.py"]