FROM python:3.10-slim

ARG RUN_ID

WORKDIR /app

RUN echo "Downloading model for RUN_ID=${RUN_ID}"

CMD ["sh", "-c", "echo Model container ready for RUN_ID=${RUN_ID}"]