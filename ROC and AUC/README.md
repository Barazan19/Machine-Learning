# 🧠 Machine Learning: ROC AUC Modular Project

This project demonstrates how to build a logistic regression classifier and evaluate it using the **ROC curve** and **AUC (Area Under the Curve)** metric. The project is modularized using Python scripts for better code reuse and organization.

---

## 📁 Folder Structure

```
Machine Learning/ROC and AUC/
├── data/
│   └── insurance_claim_dataset.csv         # Place your dataset here
├── modules/
│   ├── data_loader.py        # Functions to load data
│   └── model_utils.py        # Functions to train model, compute ROC-AUC, and find optimal threshold
└── notebooks/
    └── roc_auc_modular.py    # Main analysis notebook/script
```

---

## 🚀 How to Use

1. Clone this repo or copy the folder structure.
2. Place your dataset (e.g. `nsurance_claim_dataset.csv`) in the `data/` folder. The dataset should have a target column named `claim`.
3. Run the notebook or Python script located in `notebooks/roc_auc_modular.py`.
4. The script will:
   - Load the data
   - Train a Logistic Regression model
   - Plot the ROC curve
   - Calculate AUC score
   - Find the **optimal classification threshold** using Youden’s J statistic

---

## 📦 Requirements

Make sure you have these Python packages installed:

- pandas
- scikit-learn
- matplotlib
- numpy

You can install them with:

```bash
pip install pandas scikit-learn matplotlib numpy
```

---

## 📈 Output

- ROC Curve with AUC score plotted
- Optimal classification threshold printed in console

---

## ✍️ Author

Made by [@Barazan19](https://github.com/Barazan19)

