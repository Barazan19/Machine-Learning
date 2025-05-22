# Insurance Claim Classifier - Modularized Version

from modules.data_loader import load_data
from modules.model_utils import split_data, train_model, evaluate_model

# Load dataset
df = load_data("data/insurance.csv")

# Prepare and split dataset
X_train, X_test, y_train, y_test = split_data(df, target_column="claim")

# Train model
model = train_model(X_train, y_train)

# Evaluate
evaluate_model(model, X_test, y_test)
