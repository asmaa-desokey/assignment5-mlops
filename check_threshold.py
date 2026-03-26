import os
import sys
import mlflow
from mlflow.tracking import MlflowClient


THRESHOLD = 0.85


def main():
    tracking_uri = os.environ.get("MLFLOW_TRACKING_URI")
    if tracking_uri:
        mlflow.set_tracking_uri(tracking_uri)

    with open("model_info.txt", "r") as f:
        run_id = f.read().strip()

    client = MlflowClient()
    run = client.get_run(run_id)

    accuracy = run.data.metrics.get("accuracy")

    if accuracy is None:
        print("ERROR: accuracy metric not found in MLflow run.")
        sys.exit(1)

    print(f"Run ID: {run_id}")
    print(f"Accuracy: {accuracy}")
    print(f"Threshold: {THRESHOLD}")

    if accuracy < THRESHOLD:
        print("Deployment failed: accuracy is below threshold.")
        sys.exit(1)

    print("Deployment passed: accuracy meets threshold.")


if __name__ == "__main__":
    main()