# 📘 Linear Regression with Gradient Descent (Real-Scale Data)

This project demonstrates the fundamentals of **Linear Regression** using **Gradient Descent** on real insurance data. The key difference: we use the data **without normalization**, allowing for interpretation in real-world units (e.g., age in years, charges in USD).

---

## 🔍 Highlights

- 📈 Visualizes how the regression line fits the real-world dataset (`age` vs `charges`)
- ⚙️ Uses gradient descent to iteratively update `w` (slope) and `b` (intercept)
- 📉 Shows how MSE (Mean Squared Error) is minimized across epochs
- 📊 Dual visualization per epoch:
  - **Left plot:** Data points + current regression line
  - **Right plot:** MSE vs `w` curve with:
    - 🔴 Current `(w, MSE)` point
    - 🟢 Tangent line (true slope at that point)
    - 🔻 Historical gradient descent path

---

## 📐 Why Without Normalization?

- Interpret the model directly:  
  _e.g., `charges = 2603.27 × age + 2377.45`_
- Better intuition for how learning rate needs to adapt to real value ranges
- Easier to explain to non-technical stakeholders

---

## ⚠️ Important Note on Interactivity

> 🛑 **This notebook uses interactive sliders (`ipywidgets`)**, which **won’t run in GitHub preview**.

To see the visualization in action, please open the notebook with one of these:

- ✅ **Jupyter Notebook** (local)
- ✅ **VSCode** with the Jupyter extension
- ✅ **Google Colab** (easy and fast)

### 🔗 Open in Colab  
[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Barazan19/Machine-Learning/blob/main/Linear%20Regression/Interactive_Linear_Regression_Slider.ipynb)

---

## 🧪 Try It Yourself

- 🔄 Use the **epoch slider** to watch the regression line and descent path update
- 🔧 Modify learning rate (`lr`) or number of epochs to test convergence
- 🧠 Observe how the tangent line and loss curve behave as training progresses

---

## 📂 Files

- `The Idea of fitting a line to data.ipynb` : step by step on how to get final slope and intercept
- `Interactive_Linear_Regression_Slider.ipynb`: interactive notebook with slider
- `insurance.csv`: dataset used (real-world insurance data)

---

## 📌 Preview

---

Made by [@Barazan19](https://github.com/Barazan19)
