
# Linear Regression from Scratch using Gradient Descent

This project demonstrates how to implement a simple **linear regression model** from scratch using **gradient descent**, inspired by [StatQuest's Gradient Descent Step-by-Step video](https://www.youtube.com/watch?v=sDv4f4s2SB8&list=PLblh5JKOoLUICTaGLRoHQDuF_7q2GfuJF&index=56).

We use the `insurance.csv` dataset and focus on predicting **charges** based on **age** using only **NumPy and Matplotlib**, no machine learning libraries like `scikit-learn`.

---

## 📁 Dataset

- Source: `insurance.csv`
- Columns used in this demo:
  - `age` (independent variable)
  - `charges` (dependent variable / target)

---

## 🧠 What You’ll Learn

1. How to **visualize data** before modeling
2. How to define and minimize the **Mean Squared Error (MSE)**
3. How **gradient descent** is used to update weights
4. Visual intuition behind **loss landscape (MSE vs weight)**

---

## 🔢 Steps Breakdown

### Step 1: Load and Visualize Data
Scatter plot showing relation between age and charges.

### Step 2: Define MSE and Prediction Function
Use the formula:  
\[
\text{MSE} = \frac{1}{n} \sum (y_{true} - y_{pred})^2
\]

### Step 3: Implement Gradient Descent
Update rules:
- \( w = w - lpha \cdot \frac{dL}{dw} \)
- \( b = b - lpha \cdot \frac{dL}{db} \)

Where:
- \( lpha \) is the learning rate

### Step 4: Plot the Fitted Regression Line
Shows how well the model fits the data after training.

### Step 5: Plot the Gradient Descent Path
Visualize the MSE as a function of weight \( w \), holding bias \( b \) fixed.  
This helps understand how gradient descent “descends” the MSE curve.

---

## 📊 Final Model

- **Final weight (slope)**: ~328.80  
- **Final bias (intercept)**: ~21.13  
- **Loss function**: MSE minimized using 200 epochs

---

## 🚀 Run It Yourself

Make sure you have:

```bash
pip install numpy matplotlib pandas
```

Then open the Jupyter notebook:

```bash
jupyter notebook Linear_Regression_Gradient_Descent_Updated.ipynb
```

---

## 🧠 Inspiration

This notebook follows the visual intuition and clarity from Josh Starmer’s [StatQuest channel](https://www.youtube.com/user/joshstarmer).

---

## 📎 Files Included

- `insurance.csv` – dataset
- `Linear_Regression_Gradient_Descent_Updated.ipynb` – full notebook
- `README.md` – project documentation

---

## ✅ License

Feel free to use and fork this repo for learning purposes!
