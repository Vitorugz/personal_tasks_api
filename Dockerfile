FROM python:alpine

WORKDIR /app

COPY . .

RUN apt-get update && apt-get install -y gcc libpq-dev && \
    pip install -r requirements.txt && \
    apt-get remove -y gcc && apt-get autoremove -y && apt-get clean

CMD ["python", "run.py"]
