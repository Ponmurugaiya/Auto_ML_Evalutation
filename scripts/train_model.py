import pandas as pd
from imblearn.under_sampling import RandomUnderSampler
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score, precision_score, recall_score, f1_score
import joblib
from datetime import datetime
from report_generator import generate_html_report
import os

# Load dataset
df = pd.read_csv('./datasets/creditcard.csv')

# Separate features and target variable
X = df.drop('Class', axis=1)
y = df['Class']

# Create an object of the class RandomUnderSampler
rus = RandomUnderSampler(random_state=42)

# Fit and apply the transform
X_resampled, y_resampled = rus.fit_resample(X, y)

# Create a new DataFrame with the resampled data
df_resampled = pd.concat([X_resampled, y_resampled], axis=1)

# Save the resampled DataFrame to a new CSV file
df_resampled.to_csv('./datasets/creditcardfraud_resampled.csv', index=False)

X_train, X_test, y_train, y_test = train_test_split(X_resampled, y_resampled, test_size=0.2, random_state=42)

# Train model with optimized parameters
model = RandomForestClassifier(
    random_state=42,
    n_estimators=50,      # Fewer trees
    max_depth=10,         # Limit tree depth
    max_features='sqrt',  # Use a subset of features
    n_jobs=-1,
    verbose=1
)
model.fit(X_train, y_train)

# Evaluate on test data
y_pred = model.predict(X_test)
print("Classification Report:")
print(classification_report(y_test, y_pred))

# Use the Jenkins workspace directory as the base path
workspace_base = os.getenv('WORKSPACE', os.getcwd())

# Define absolute paths
output_directory = os.path.join(workspace_base, 'workspace/models')
os.makedirs(output_directory, exist_ok=True)

# Save the model
output_path = os.path.join(output_directory, 'random_forest_model.pkl')
joblib.dump(model, output_path)

metrics = {
    'date': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
    'model_name': 'Random Forest Classifier',
    'dataset': 'creditcard.csv',
    'performance': {
        'Accuracy': accuracy_score,
        'Precision': precision_score,
        'Recall': recall_score,
        'F1 Score': f1_score
        }
}

# Generate the report
output_dir = os.path.join(workspace_base, 'output')
os.makedirs(output_dir, exist_ok=True)
output_file = os.path.join(output_dir, 'model_training_report.html')
generate_html_report(metrics, output_file)



