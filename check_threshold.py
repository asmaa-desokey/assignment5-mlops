import os
import sys
import mlflow
from mlflow.tracking import MlflowClient

mlflow.set_tracking_uri(os.getenv("MLFLOW_TRACKING_URI"))

THRESHOLD = 0.85

# Read Run ID
with open("model_info.txt", "r") as f:
    run_id = f.read().strip()

client = MlflowClient()

run = client.get_run(run_id)

accuracy = run.data.metrics["accuracy"]

print("Accuracy:", accuracy)

if accuracy < THRESHOLD:
    print("Accuracy below threshold. Failing pipeline.")
    sys.exit(1)

print("Model passed threshold.")