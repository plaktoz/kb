# Machine Learning Algorithms Overview

A practical tour of the core ML algorithms — what each does, when to use it, and how they relate to one another. Organized by learning type.

## Taxonomy

```
Machine Learning
├── Supervised Learning
│   ├── Regression (continuous target)
│   │   ├── Linear Regression
│   │   └── KNN (regression mode)
│   └── Classification (categorical target)
│       ├── Logistic Regression
│       ├── K-Nearest Neighbors (KNN)
│       ├── Support Vector Machine (SVM)
│       ├── Naive Bayes
│       ├── Decision Trees
│       └── Ensemble Methods
│           ├── Bagging → Random Forest
│           └── Boosting → AdaBoost, Gradient Boosting, XGBoost
│       └── Neural Networks / Deep Learning
└── Unsupervised Learning
    ├── Clustering → K-Means, Hierarchical, DBSCAN
    └── Dimensionality Reduction → PCA
```

## Supervised Learning Algorithms

### Linear Regression
- **What**: Fits a linear equation to minimize the sum of squared residuals (distances between data points and the regression line).
- **Use**: Predicting a continuous numeric target (e.g. house price from square footage).
- **Key idea**: The simplest model — many advanced algorithms (including neural networks) are extensions of this idea.

### Logistic Regression
- **What**: A variant of linear regression that fits a **sigmoid function** instead of a line; outputs a class *probability*.
- **Use**: Binary classification (e.g. spam/not spam, male/female given height & weight).
- **Key idea**: Despite the name, it is a classifier, not a regressor.

### K-Nearest Neighbors (KNN)
- **What**: Non-parametric — no model is explicitly fitted. For a new data point, predicts based on the K closest training examples (majority vote for classification; average for regression).
- **Hyperparameter**: K. Small K → overfitting; large K → underfitting.
- **Use**: Both regression and classification; powerful when relationships are nonlinear.

### Support Vector Machine (SVM)
- **What**: Finds the decision boundary (line/hyperplane) that maximizes the **margin** between classes. The training points on the margin edge are **support vectors**.
- **Kernel trick**: Implicitly maps features into higher-dimensional space to create nonlinear boundaries (RBF, polynomial, sigmoid kernels) — this is *implicit feature engineering*.
- **Strengths**: Works well in high dimensions; memory efficient (only support vectors matter); robust to outliers due to margin maximization.
- **Use**: Classification and regression, especially high-dimensional problems.

### Naive Bayes
- **What**: Applies Bayes' theorem, multiplying per-feature probabilities. "Naive" = assumes features are independent (often false but computationally efficient).
- **Use**: Text classification, spam filters, fast baseline classifiers.

### Decision Trees
- **What**: Recursively splits data via yes/no questions to create **leaf nodes** that are as pure (homogeneous) as possible.
- **Limitation**: Prone to overfitting on its own; powerful as the base for ensemble methods.
- **Use**: Foundation for random forests and boosting.

### Ensemble Methods

#### Bagging → Random Forest
- **Bagging**: Train multiple models on different bootstrap (random with replacement) subsets of training data; aggregate by majority vote or average.
- **Random Forest**: Bagging applied to decision trees, with the added twist of randomly excluding features per tree. Prevents correlation between trees and reduces overfitting.
- **Use**: Both classification and regression; robust, general-purpose.

#### Boosting → AdaBoost / Gradient Boosting / XGBoost
- **Boosting**: Train models *sequentially* — each model corrects the errors of the previous one. Combines weak learners into a strong learner.
- **vs Bagging**: Boosted trees often reach higher accuracy but are slower to train and more prone to overfitting.
- **Famous implementations**: AdaBoost, Gradient Boosting, XGBoost.

### Neural Networks / Deep Learning
- **Single-layer perceptron**: Essentially multi-feature logistic/linear regression.
- **Hidden layers**: Variables between input and output that represent *automatically learned features* (implicit feature engineering, similar to SVM kernels but far more expressive).
- **Deep learning**: Many hidden layers → hierarchical feature representations (edges → shapes → faces, etc.). The model learns *what features matter* without human guidance.
- **Why powerful**: Can represent arbitrarily complex mappings; drives most recent AI advances.
- **Trade-off**: Requires large data and compute; less interpretable.

## Unsupervised Learning Algorithms

### K-Means Clustering
- **What**: Assigns each data point to one of K clusters by iteratively: (1) assign points to nearest centroid, (2) recompute centroids, until stable.
- **Key distinction from classification**: No labels exist; the algorithm discovers structure.
- **Hyperparameter**: K (number of clusters). Choice requires domain knowledge and trial-and-error.
- **Alternatives**: Hierarchical clustering, DBSCAN (finds clusters of arbitrary shape; does not require specifying K).

### Principal Component Analysis (PCA)
- **What**: Finds directions of maximum variance (principal components), orthogonal to each other. Projects data onto the top-K components, discarding low-variance dimensions.
- **Use**: Dimensionality reduction — removes correlated/redundant features, reduces noise, speeds up downstream models.
- **Example**: Height and length of fish are correlated → combine into a single "shape" feature.

## Algorithm Selection Heuristic

| Question | Direction |
|----------|-----------|
| Do I have labeled data? | Yes → supervised; No → unsupervised |
| Predicting a number? | Regression (linear regression, KNN, random forest) |
| Predicting a category? | Classification (logistic regression, SVM, random forest, neural net) |
| Finding groups with no labels? | Clustering (K-means, DBSCAN) |
| Too many features? | Dimensionality reduction (PCA) first |
| Need interpretability? | Decision trees, linear/logistic regression |
| Need high accuracy, big data? | Gradient boosting, neural networks |

Scikit-learn provides a published algorithm selection cheat sheet for further guidance.

## Related Notes

- [[machine-learning-concepts-glossary]] — full vocabulary (bias, variance, overfitting, gradient descent, etc.)

## Source

Video: *All Machine Learning Algorithms Explained in 17 Min* — Infinite Codes / Tim (2024)
URL: https://www.youtube.com/watch?v=E0Hmnixke2g
