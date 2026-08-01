# Machine Learning Concepts Glossary

A concise reference for foundational ML terminology, covering the full vocabulary from raw data to model evaluation.

## Core Distinctions

- **AI vs Machine Learning**: AI encompasses any system mimicking human cognition (including rule-based systems). ML is a *subset* of AI where models learn patterns from data rather than following explicit rules.
- **Algorithm**: A deterministic set of step-by-step instructions to solve a problem (e.g. Dijkstra's shortest path). In ML, algorithms learn from data to produce a *model*.
- **Model**: The trained artifact — a mathematical mapping from input features to output predictions (e.g. the slope + intercept of a fitted regression line).

## Learning Paradigms

| Paradigm | Labels provided? | Typical use |
|----------|----------------|------------|
| **Supervised** | Yes (input + correct output) | ~70% of ML applications — classification, regression |
| **Unsupervised** | No | Clustering, pattern discovery |
| **Reinforcement** | No labels; reward/penalty signal | Game playing, robotics, sequential decisions |

## Data Vocabulary

- **Feature** (input / independent variable / predictor): A measurable property used as model input (e.g. square footage, number of bedrooms).
- **Target** (output / label / dependent variable): What the model predicts (e.g. house price, spam/not-spam).
- **Instance** (sample / observation / data point): One row in a dataset — all features + target for a single example.
- **Label**: The known correct output for an instance in supervised learning; obtaining labels is often the main bottleneck.
- **Training data**: Labeled examples used to fit the model.
- **Test data**: A completely held-out set used *once* at the end to estimate real-world performance. Inadvertent inclusion of test data during training is called **data leakage**.
- **Validation set / Cross-validation**: Held-out slice used *during* development to tune hyperparameters. In k-fold CV the data is split into k parts; the model trains k times, each time using a different fold as validation.

## Pre-processing

- **Feature engineering**: Creating new, more informative features from raw data (e.g. deriving `is_holiday` from a date column).
- **Feature scaling** (normalization / standardization): Transforming numeric features to a common scale so large-magnitude features don't dominate (e.g. min-max to [0,1] or z-score standardization).
- **Dimensionality**: The number of features. High-dimensional data creates sparsity — the *curse of dimensionality* — making patterns harder to find and necessitating dimensionality reduction.

## Training Mechanics

- **Model fitting** (training / learning): Adjusting model parameters to minimize prediction error on training data.
- **Parameter** (weight): A value learned from data during training (e.g. the slope in linear regression). Modern deep learning models have millions to billions of parameters.
- **Hyperparameter**: A configuration set *before* training that controls the learning process (e.g. learning rate, batch size, number of layers). Finding optimal values requires experimentation.
- **Batch**: A subset of training data processed in one update step. Larger batches are more stable but memory-intensive; smaller batches update more frequently.
- **Epoch**: One complete pass through the entire training dataset. Too many epochs → overfitting.
- **Iteration**: One pass through one batch → one parameter update.
- **Cost function** (loss / objective function): Measures prediction error (e.g. mean squared error). Training minimizes this.
- **Gradient descent**: Optimization algorithm that iteratively moves parameters in the direction of steepest error decrease. The step size is the *learning rate*. Can get stuck in local minima; **momentum-based gradient descent** adds inertia to escape them.
- **Learning rate**: Hyperparameter controlling the size of each parameter update. Too high → divergence; too low → slow convergence or local minima.
- **Regularization**: Penalties that keep parameters small to prevent overfitting (e.g. L1/L2). Strength is a hyperparameter — too much causes underfitting.

## Model Complexity & Generalization

- **Model complexity**: Number and flexibility of parameters. Higher-order polynomials are more complex than linear models.
- **Bias**: Error from overly rigid assumptions. High-bias models (e.g. linear regression on curved data) underfit.
- **Variance**: Sensitivity to changes in training data. High-variance models overfit noise.
- **Bias–variance tradeoff**: As complexity increases, bias decreases but variance increases. The optimal model balances both — capturing true patterns without fitting noise.
- **Noise**: Random fluctuations in data that don't reflect true underlying patterns.
- **Overfitting**: Model memorizes training noise; performs well on training data but poorly on new data (high variance).
- **Underfitting**: Model is too simple to capture real patterns; performs poorly on both training and test data (high bias).

## Evaluation

- **Evaluation metrics**: Accuracy, precision, recall, F1 (classification); MSE, R² (regression).
- **Validation** prevents premature overfitting during development; the **test set** provides final unbiased performance estimates.

## Related Notes

- [[machine-learning-algorithms-overview]] — concrete algorithm catalogue (linear regression through deep learning)

## Source

Video: *All Basic Machine Learning Terms Explained in 22 Minutes* — Infinite Codes (2024)
URL: https://www.youtube.com/watch?v=Fa_V9fP2tpU
