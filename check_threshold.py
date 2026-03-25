import sys
import mlflow
from mlflow.tracking import MlflowClient

THRESHOLD = 0.85

mlflow.set_tracking_uri("file:./mlruns")

with open("model_info.txt", "r", encoding="utf-8") as f:
    run_id = f.read().strip()

client = MlflowClient()
run = client.get_run(run_id)

accuracy = run.data.metrics.get("accuracy")

print("Run ID:", run_id)
print("Accuracy:", accuracy)
print("Threshold:", THRESHOLD)

if accuracy is None:
    print("No accuracy metric found.")
    sys.exit(1)

if accuracy < THRESHOLD:
    print("Deployment failed: accuracy below threshold.")
    sys.exit(1)

print("Deployment passed: accuracy meets threshold.")