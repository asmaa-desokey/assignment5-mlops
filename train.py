<<<<<<< HEAD
=======
import os
>>>>>>> e9f2b0cd8a8a966081178761bef57d67fc516064
import mlflow
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
<<<<<<< HEAD

mlflow.set_tracking_uri("file:./mlruns")
=======
import mlflow
mlflow.set_tracking_uri("file:./mlruns")
tracking_uri = os.environ.get("MLFLOW_TRACKING_URI", "file:./mlruns")
mlflow.set_tracking_uri(tracking_uri)

>>>>>>> e9f2b0cd8a8a966081178761bef57d67fc516064
mlflow.set_experiment("mlops-assignment")

X, y = load_iris(return_X_y=True)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

with mlflow.start_run() as run:
    model = LogisticRegression(max_iter=200)
    model.fit(X_train, y_train)

    predictions = model.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)

    mlflow.log_metric("accuracy", accuracy)

    run_id = run.info.run_id

    with open("model_info.txt", "w", encoding="utf-8") as f:
        f.write(run_id)

    print("Run ID:", run_id)
    print("Accuracy:", accuracy)