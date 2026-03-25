import sys
import mlflow
from mlflow.tracking import MlflowClient
<<<<<<< HEAD

THRESHOLD = 0.85

mlflow.set_tracking_uri("file:./mlruns")
=======
import mlflow
mlflow.set_tracking_uri("file:./mlruns")
THRESHOLD = 0.85
>>>>>>> e9f2b0cd8a8a966081178761bef57d67fc516064

with open("model_info.txt", "r", encoding="utf-8") as f:
    run_id = f.read().strip()

client = MlflowClient()
run = client.get_run(run_id)

accuracy = run.data.metrics.get("accuracy")

<<<<<<< HEAD
print("Run ID:", run_id)
print("Accuracy:", accuracy)

if accuracy is None:
    print("No accuracy metric found.")
    sys.exit(1)

if accuracy < THRESHOLD:
    print("Deployment failed: accuracy below threshold.")
    sys.exit(1)

print("Deployment passed: accuracy meets threshold.")
=======
if accuracy is None:
    print("Accuracy metric not found.")
    sys.exit(1)

print("Accuracy:", accuracy)

if accuracy < THRESHOLD:
    print("Accuracy below threshold. Failing pipeline.")
    sys.exit(1)

print("Model passed threshold.")
>>>>>>> e9f2b0cd8a8a966081178761bef57d67fc516064
