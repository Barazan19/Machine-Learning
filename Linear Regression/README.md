# Linear Regression

This repository provides a step-by-step, visual, and intuitive exploration of **linear regression using gradient descent**, from scratch and with Scikit-Learn, along with experiments on normalization, hyperparameter tuning, and interactive visualizations.

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

### 1. [`The Idea of fitting a line to data.ipynb`](https://colab.research.google.com/drive/your_link_here)
This notebook demonstrates **how gradient descent works manually** to fit a linear regression model, **without normalization**. It shows how we compute gradients, update weights, and minimize the Mean Squared Error (MSE) step by step.

### 2. [`The Idea of fitting a line to data with normalization.ipynb`](https://colab.research.google.com/drive/your_link_here)
Here we introduce **normalization** to the same process to see its **impact on convergence**. You’ll observe how scaling the feature (age) helps the gradient descent converge faster and more stably.

### 3. [`Interactive_Linear_Regression_Slider.ipynb`](https://colab.research.google.com/drive/your_link_here)
An **interactive slider visualization** using `ipywidgets` that allows you to explore how the line changes over iterations. This is useful for visualizing the learning dynamics of gradient descent in real-time.

### 4. [`The Idea of fitting a line to data with scikit-learn.ipynb`](https://colab.research.google.com/drive/your_link_here)
To compare our manual implementation, we use **Scikit-Learn’s `LinearRegression`**. The result was noticeably different at first, most likely because:
- The **learning rate** was too low
- The **number of epochs** was too few
- Manual gradient descent can stop early or converge to suboptimal values without proper tuning

Scikit-Learn uses a **closed-form solution** via the Normal Equation:

**Normal Equation** used in Scikit-Learn:

> **β̂ = (XᵀX)⁻¹ Xᵀ y**


This means it reaches the optimal result directly, without iteration.

### 5. [`The Idea of fitting a line to data adjusted epoch lr.ipynb`](https://colab.research.google.com/drive/your_link_here)
In this final notebook, we **adjust the learning rate and epoch count** to improve the accuracy of our manual gradient descent. We also implement **early stopping** to prevent overfitting or excessive iterations. As a result, the model gets **much closer to Scikit-Learn’s output**.

---

## 📌 Summary

| Notebook | Focus |
|----------|-------|
| `The Idea of fitting a line to data.ipynb` | Manual gradient descent without normalization |
| `...with normalization.ipynb` | Impact of normalization |
| `...Slider.ipynb` | Interactive visualization of gradient descent |
| `...with scikit-learn.ipynb` | Comparison with closed-form solution |
| `...adjusted epoch lr.ipynb` | Tuning learning rate and epochs for better results |

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

![image](https://github.com/user-attachments/assets/b3234085-d336-4413-a73c-a93c86dd3c0d)
![image](https://github.com/user-attachments/assets/87edd1f9-5121-4f6e-a2df-2eb88c598aa8)


---

## 🧠 Author

Made by Barazan19, to learn and visualize machine learning intuitively from first principles.

