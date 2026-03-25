FROM python:3.10-slim

ARG RUN_ID

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

RUN echo "Downloading model for RUN_ID=${RUN_ID}"

CMD ["echo", "Model container ready"]