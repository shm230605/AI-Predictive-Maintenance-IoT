from src.model import train_model, evaluate_model
from src.feature_importance import plot_feature_importance
from src.roc_curve import plot_roc_curve
from src.evaluation import plot_confusion_matrix

print("📥 Training Model...")

model, X_test, y_test = train_model()   # ✅ NO PARAMETERS

print("📊 Evaluating Model...")
evaluate_model(model, X_test, y_test)

print("📈 Feature Importance...")
plot_feature_importance()

print("📊 ROC Curve...")
plot_roc_curve(X_test, y_test)

print("📉 Confusion Matrix...")
plot_confusion_matrix(X_test, y_test)

print("✅ DONE")