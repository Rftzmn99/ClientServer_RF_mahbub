
FROM python:3.11-slim

WORKDIR /usr/src/app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 50051

CMD ["python", "server/server.py"]
