# Machine-Learning
My journey on learning Machine Learning from various sources

## 🧠 Machine Learning Algorithm Summary

This section provides a high-level overview of the most widely-used Machine Learning algorithms, including their strengths, weaknesses, and common hyperparameters.

| **Name**               | **Method**            | **Strengths**                                         | **Weaknesses**                                        | **Key Parameters**                                   |
|------------------------|------------------------|--------------------------------------------------------|--------------------------------------------------------|--------------------------------------------------------|
| **Linear Regression**  | Regression             | Simple, fast, interpretable                           | Assumes linearity, sensitive to outliers              | `fit_intercept`, `normalize`                          |
| **Logistic Regression**| Classification         | Probabilistic output, efficient                       | Only linear decision boundaries                        | `penalty`, `C`, `solver`                              |
| **Decision Tree**      | Both                   | Interpretable, handles non-linear data                | Overfitting, unstable                                  | `max_depth`, `min_samples_split`, `criterion`         |
| **Random Forest**      | Both                   | Reduces overfitting, robust                           | Less interpretable                                     | `n_estimators`, `max_depth`, `max_features`           |
| **Gradient Boosting**  | Both                   | High accuracy, handles various data types             | Slow training                                          | `learning_rate`, `n_estimators`, `max_depth`          |
| **Support Vector Machine (SVM)** | Both         | Effective in high dimensions                          | Memory intensive, needs tuning                        | `C`, `kernel`, `gamma`                                |
| **Naive Bayes**        | Classification         | Simple, fast                                          | Strong independence assumption                         | `var_smoothing`                                       |
| **K-Nearest Neighbors (KNN)** | Both           | Simple, no training phase                             | Slow prediction, sensitive to irrelevant features      | `n_neighbors`, `weights`, `metric`                    |
| **K-Means**            | Clustering             | Efficient, simple                                     | Needs to specify `k`, sensitive to scale               | `n_clusters`, `init`, `max_iter`                      |
| **DBSCAN**             | Clustering             | Doesn’t require `k`, finds arbitrarily shaped clusters| Hard to choose `eps`                                   | `eps`, `min_samples`                                  |
| **PCA**                | Dimensionality Reduction| Reduces dimensionality, improves visualization        | Loses interpretability                                 | `n_components`                                        |
| **Neural Networks**    | Both                   | Handles complex patterns                              | Needs lots of data, computationally expensive          | `layers`, `learning_rate`, `epochs`, `batch_size`     |

---

📌 _This cheat sheet is part of the repository to summarize key ML algorithms for quick reference._

🛠️ _Made by **Barazan19**, to learn and visualize machine learning intuitively from first principles._
