FROM python:3.9-slim

RUN apt-get update && apt-get install -y \
    default-jre \
    fastqc \
 && apt-get clean && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY main.py requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

ENTRYPOINT ["python", "main.py"]
