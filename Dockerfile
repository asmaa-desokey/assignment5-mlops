FROM python:3.10-slim

ARG RUN_ID
<<<<<<< HEAD
ENV RUN_ID=${RUN_ID}

WORKDIR /app

RUN echo "Preparing container for MLflow Run ID: ${RUN_ID}"
CMD echo "Downloading model for Run ID: ${RUN_ID} (mock)"
=======

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

RUN echo "Downloading model for RUN_ID=${RUN_ID}"

CMD ["echo", "Model container ready"]
>>>>>>> e9f2b0cd8a8a966081178761bef57d67fc516064
