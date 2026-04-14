import matplotlib.pyplot as plt
import pandas as pd
import joblib

def plot_feature_importance(model_path="models/model.pkl"):
    model = joblib.load(model_path)

    features = ["temperature", "vibration", "current"]
    importance = model.feature_importances_

    df = pd.DataFrame({
        "Feature": features,
        "Importance": importance
    })

    df = df.sort_values(by="Importance")

    plt.figure()
    plt.barh(df["Feature"], df["Importance"])
    plt.title("Feature Importance (AI Decision Factors)")
    plt.xlabel("Importance Score")

    plt.tight_layout()
    plt.savefig("images/feature_importance.png")
    plt.show()