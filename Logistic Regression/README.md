# 🧠 Logistic Regression from Scratch (1 Feature Only — Manual Gradient Descent)

This repository demonstrates a step-by-step implementation of **Logistic Regression from scratch** using only Python — no machine learning libraries involved.

We explore the logistic function, gradient descent, cross-entropy loss, and how changing the slope (θ₁) affects the shape of the sigmoid curve.

---

## 📁 Project Structure

The notebook is organized into the following sections:

- 📥 Step 1: Load and Visualize Data
- 🧼 Step 2: Normalize Input Feature
- ⚙️ Step 3: Sigmoid Function
- 🎯 Step 4: Loss Function (Binary Cross-Entropy)
- ✏️ Step 5: Gradient Derivation
- 🔁 Step 6: Training Loop with Gradient Descent
- 📉 Step 7: Visualize Cost Function
- 📈 Step 8: Visualize Fitted Sigmoid Curve
- ✅ Final Summary
- 🔍 Why Does the Sigmoid Curve Not Look Asymptotic in Age vs Probability?
- 🧠 Explanation:
- 🧪 Simulation: What Happens if θ₁ is Larger?
- ✅ So Which Model Is Better?
- Verdict:
- 🎨 Visual Comparison of Sigmoid Curves with Varying Slopes
- ✅ Final Conclusion
- 🔹 Model Results
- 🔹 Curve Behavior
- 🔹 What This Tells Us
- 🧪 Next Steps

---

## 🔍 What You'll Learn

- How logistic regression works under the hood
- How to derive and apply the gradient for cross-entropy loss
- Why sigmoid curves can appear "non-asymptotic" depending on θ₁
- How slope affects decision boundary sharpness
- Practical intuition for model fitting and generalization

---

## 📊 Dataset

We use a custom insurance claim dataset with the following feature:
- **Age** (normalized)
- **Claim** (binary target)

You can find it inside the `Insurance_Claim_Dataset.csv` file.

---

## 🧪 Bonus Simulation

We demonstrate the impact of different values of **θ₁** (slope) on the sigmoid curve:
- θ₁ = 0.7 (trained)
- θ₁ = 2, 5, 10, 20 (manual test)

This helps illustrate how the model's decision boundary changes based on confidence level.

---

## ✅ How to Run

1. Clone the repo
2. Make sure `matplotlib`, `numpy`, and `pandas` are installed
3. Open the `.ipynb` file in Jupyter Notebook or VS Code
4. Run all cells and explore step-by-step

---

## 🧠 Author Notes

This project is built for educational purposes and to strengthen fundamental understanding of logistic regression by deriving it mathematically and implementing it manually.

Feel free to fork or adapt it into your own ML learning path!

---
