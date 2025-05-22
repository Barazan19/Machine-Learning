from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score, roc_curve
import numpy as np

def train_model(X_train, y_train):
    model = LogisticRegression()
    model.fit(X_train, y_train)
    return model

def get_roc_auc(model, X_test, y_test):
    y_prob = model.predict_proba(X_test)[:,1]
    auc = roc_auc_score(y_test, y_prob)
    fpr, tpr, thresholds = roc_curve(y_test, y_prob)
    return auc, fpr, tpr, thresholds

def find_optimal_threshold(fpr, tpr, thresholds):
    youden_index = tpr - fpr
    optimal_idx = np.argmax(youden_index)
    return thresholds[optimal_idx]
