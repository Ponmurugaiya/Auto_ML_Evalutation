import pandas as pd
import joblib
from sklearn.metrics import classification_report, confusion_matrix, roc_auc_score, roc_curve
import seaborn as sns
import matplotlib.pyplot as plt

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

# Confusion Matrix
cm = confusion_matrix(y, y_pred)
sns.heatmap(cm, annot=True, fmt="d", cmap="Blues")
plt.title("Confusion Matrix")
plt.savefig('./reports/confusion_matrix.png')
plt.clf()

# ROC Curve
fpr, tpr, _ = roc_curve(y, y_proba)
plt.plot(fpr, tpr, label="ROC Curve")
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.title("ROC Curve")
plt.legend()
plt.savefig('./reports/roc_curve.png')
plt.clf()
