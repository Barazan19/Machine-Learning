# Logistic Regression 🚦

This notebook suite implements **Logistic Regression** from scratch, focusing on intuitive understanding and step-by-step development. It mirrors the structure of the Linear Regression folder, but adapted to classification context.

---

## 📚 Table of Contents

- [📁 File Overview](#-file-overview)
- [📌 Summary](#-summary)
- [🚀 Run in Google Colab](#-run-in-google-colab)
- [⚙️ Requirements](#️-requirements)
- [📷 Sample Result](#-sample-result)
- [🧠 Author](#-author)
---
## 📁 File Overview

### 1. [The_Idea_of_fitting_a_sigmoid_to_data.ipynb](https://colab.research.google.com/drive/your_link_here)  
 This notebook demonstrates **how gradient descent on sigmoid function works manually** to fit a logistic regression model, **without normalization**. It shows how we compute gradients, update weights, and minimize the Log Loss step by step.

### 2. [The_Idea_of_fitting_a_sigmoid_to_data_NORMALIZE.ipynb](https://colab.research.google.com/drive/your_link_here)  
  Same as above but using manual normalization of the `Age` feature — compare convergence with and without feature scaling.

### 3. [The_Idea_of_fitting_a_sigmoid_to_data_scikit_learn.ipynb](https://colab.research.google.com/drive/your_link_here)
  Logistic Regression using `scikit-learn`: loading data, training, evaluating metrics (log-loss, confusion matrix, accuracy), and plotting the fitted sigmoid.

### 4. [Interactive_Logistic_Regression_Epoch_Slider.ipynb](https://colab.research.google.com/drive/your_link_here)
  Explore how the sigmoid curve evolves epoch-by-epoch via interactive slider — ideal for visualizing model training dynamics.
---

## 📌 Summary

| Notebook | Focus |
|----------|-------|
| `The Idea of fitting a sigmoid to data.ipynb` | Manual gradient descent without normalization |
| `...with normalization.ipynb` | Impact of normalization |
| `...Slider.ipynb` | Interactive visualization of gradient descent |
| `...with scikit-learn.ipynb` | Comparison with closed-form solution |
---

## 💡 How Similar Is It to Linear Regression?

Logistic Regression shares foundational ideas with Linear Regression:

1. **Linear combination of inputs**  
   - Linear Regression:  
     `ŷ = w * x + b`  
   - Logistic Regression uses a linear term inside a sigmoid:  
     `p = sigmoid(θ₀ + θ₁ * x)`

2. **Gradient Descent optimization**  
   Both methods use gradient descent to find the best parameters by minimizing a cost function:
   - Linear: Mean Squared Error (MSE)
   - Logistic: Negative Log-Likelihood (Log-Loss)

3. **Concept of slope/intercept**  
   - Linear: slope *m* means change in `y` per unit `x`
   - Logistic: parameter θ₁ governs the change in **log-odds** per unit `x`

---

## ⚠️ Key Differences You’ll Learn

| Comparison         | Linear Regression              | Logistic Regression                             |
|--------------------|-------------------------------|--------------------------------------------------|
| Output             | Continuous (any real value)   | Probabilities (0–1) via sigmoid function         |
| Cost Function      | MSE (quadratic, smooth)       | Log-Loss (non-linear, “steep” in ends)          |
| Parameter Meaning  | Additive effect on `y`        | Multiplicative effect on odds: \( e^{θ₁} \)      |
| Visualization      | 2D plot + simple contour      | 3D surface needed to fully visualize cost landscape |

---

## 🚀 Run in Google Colab

To run these notebooks interactively in Google Colab, click the links above (or upload them to your own Google Drive and open with Colab).

---
## ⚙️ Requirements

numpy
pandas
matplotlib
ipywidgets
scikit-learn

---
## 📷 Sample Result
![image](https://github.com/user-attachments/assets/1be1410f-9b9d-4a36-9563-84c4316660d4)
![image](https://github.com/user-attachments/assets/59c4d1d1-0ead-4019-a762-ad65ffd5e929)

---
## 🧠 Author

Made by Barazan19, to learn and visualize machine learning intuitively from first principles.
