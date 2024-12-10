import pandas as pd
import joblib
from sklearn.metrics import classification_report, confusion_matrix, roc_auc_score, roc_curve
import seaborn as sns
import matplotlib.pyplot as plt
import os

# Load model and dataset
model = joblib.load('./models/random_forest_model.pkl')
data = pd.read_csv('./datasets/creditcard.csv')

# Prepare data
X = data.drop(columns=['Class'])
y = data['Class']

# Predict
y_pred = model.predict(X)
y_proba = model.predict_proba(X)[:, 1]

# Metrics
print("Classification Report:")
print(classification_report(y, y_pred))

workspace_base = os.getenv('WORKSPACE', os.getcwd())
reports_dir = os.path.join(workspace_base, 'workspace/reports')

# Ensure the directory exists with proper permissions
os.makedirs(reports_dir, exist_ok=True)


confusion_matrix_path = os.path.join(reports_dir, 'confusion_matrix.png')
roc_curve_path = os.path.join(reports_dir, 'roc_curve.png')


# Confusion Matrix
cm = confusion_matrix(y, y_pred)
sns.heatmap(cm, annot=True, fmt="d", cmap="Blues")
plt.title("Confusion Matrix")
plt.savefig(confusion_matrix_path)
plt.clf()

# ROC Curve
fpr, tpr, _ = roc_curve(y, y_proba)
plt.plot(fpr, tpr, label="ROC Curve")
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.title("ROC Curve")
plt.legend()
plt.savefig(roc_curve_path)
plt.clf()
