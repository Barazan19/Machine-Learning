# ROC-AUC Modularized Notebook

from modules.data_loader import load_data
from modules.model_utils import train_model, get_roc_auc, find_optimal_threshold
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

# Load data
df = load_data('data/Insurance_Claim_Dataset.csv')

# Prepare features and label
X = df.drop(columns='claim')
y = df['claim']

# Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Train
model = train_model(X_train, y_train)

# ROC AUC
auc, fpr, tpr, thresholds = get_roc_auc(model, X_test, y_test)

# Optimal Threshold
optimal_threshold = find_optimal_threshold(fpr, tpr, thresholds)

# Plot ROC
plt.plot(fpr, tpr, label=f'AUC = {auc:.2f}')
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.title("ROC Curve")
plt.legend()
plt.show()

print(f"Optimal threshold: {optimal_threshold:.2f}")
