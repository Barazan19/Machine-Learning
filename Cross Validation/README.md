
# Logistic Regression with Cross-Validation

This repository demonstrates how to apply various cross-validation methods to evaluate a logistic regression model using a health insurance dataset.

## Folder Structure

```
.
├── data
│   └── insurance_claim_dataset.csv
├── model
│   └── logistic_model.py
├── cross_validation_logistic_regression.ipynb
└── README.md
```

## Cross-Validation Methods Compared

- No CV (Train-Test Split)
- K-Fold Cross-Validation
- Stratified K-Fold
- Leave-One-Out Cross-Validation (LOOCV)
- Repeated K-Fold

## Why Use Cross-Validation?

Without cross-validation, your model might look good only because it got "lucky" on one specific train/test split. Cross-validation ensures the model is tested across multiple scenarios, giving a better picture of its real-world performance.

## Result

You'll find that simple train-test split often gives higher accuracy, but that’s misleading. Cross-validation gives a more honest estimate and helps prevent overfitting.
