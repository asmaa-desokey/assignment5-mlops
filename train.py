import mlflow
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

mlflow.set_tracking_uri("file:./mlruns")
mlflow.set_experiment("mlops-assignment")

X, y = load_iris(return_X_y=True)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

with mlflow.start_run() as run:
    model = RandomForestClassifier(n_estimators=200, random_state=42)
    model.fit(X_train, y_train)

    predictions = model.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)

    mlflow.log_metric("accuracy", accuracy)

    run_id = run.info.run_id

    with open("model_info.txt", "w") as f:
        f.write(run_id)

    print("Run ID:", run_id)
    print("Accuracy:", accuracy)
