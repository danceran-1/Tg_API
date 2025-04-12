
FROM python:3.12-slim

WORKDIR /app
COPY requirements.txt .
RUN apt-get update && apt-get install -y curl
COPY . .

EXPOSE 8000

CMD ["python", "main.py","8000"]
