import joblib
import numpy as np

# Load trained model
def load_model(path="models/model.pkl"):
    model = joblib.load(path)
    return model


# Predict failure
def predict_failure(model, temperature, vibration, current):

    data = np.array([[temperature, vibration, current]])

    prediction = model.predict(data)[0]

    if prediction == 1:
        return "⚠️ Machine Failure Likely"
    else:
        return "✅ Machine is Normal"