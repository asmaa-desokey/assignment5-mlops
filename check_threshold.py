import sys
import mlflow
from mlflow.tracking import MlflowClient

THRESHOLD = 0.85

with open("model_info.txt", "r", encoding="utf-8") as f:
    run_id = f.read().strip()

client = MlflowClient()
run = client.get_run(run_id)

accuracy = run.data.metrics.get("accuracy")

if accuracy is None:
    print("Accuracy metric not found.")
    sys.exit(1)

print("Accuracy:", accuracy)

if accuracy < THRESHOLD:
    print("Accuracy below threshold. Failing pipeline.")
    sys.exit(1)

print("Model passed threshold.")