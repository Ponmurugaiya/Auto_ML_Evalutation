import pandas as pd
from imblearn.under_sampling import RandomUnderSampler
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score, precision_score, recall_score, f1_score
import joblib
from datetime import datetime
from report_generator import generate_html_report

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


# Save model
joblib.dump(model, './models/random_forest_model.pkl')

# Evaluate on test data
y_pred = model.predict(X_test)
print("Classification Report:")
print(classification_report(y_test, y_pred))

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
generate_html_report(metrics, output_file="output/model_training_report.html")