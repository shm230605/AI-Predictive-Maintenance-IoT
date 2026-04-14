import matplotlib.pyplot as plt
from sklearn.metrics import roc_curve, auc
import joblib

def plot_roc_curve(X_test, y_test, model_path="models/model.pkl"):
    model = joblib.load(model_path)

    y_prob = model.predict_proba(X_test)[:, 1]

    fpr, tpr, _ = roc_curve(y_test, y_prob)
    roc_auc = auc(fpr, tpr)

    plt.figure()
    plt.plot(fpr, tpr, label=f"AUC = {roc_auc:.2f}")
    plt.plot([0, 1], [0, 1], '--')

    plt.title("ROC Curve - Failure Prediction Performance")
    plt.xlabel("False Positive Rate")
    plt.ylabel("True Positive Rate")
    plt.legend()

    plt.tight_layout()
    plt.savefig("images/roc_curve.png")
    plt.show()