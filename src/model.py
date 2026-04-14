import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib


def train_model():
    # Load dataset
    data = pd.read_csv("data/iot_sensor_data.csv")

    # Features & target
    X = data[["temperature", "vibration", "current"]]
    y = data["failure"]

    # Split data
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # Train model
    model = RandomForestClassifier(n_estimators=100)
    model.fit(X_train, y_train)

    # Save model
    joblib.dump(model, "models/model.pkl")

    return model, X_test, y_test


def evaluate_model(model, X_test, y_test):
    y_pred = model.predict(X_test)

    acc = accuracy_score(y_test, y_pred)

    print(f"✅ Accuracy: {acc:.2f}")

    return acc