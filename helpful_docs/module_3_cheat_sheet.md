# Module 3: Supervised Learning Cheat Sheet
## Data → Model → Evaluate Pipeline

---

## 🎯 When to Use What

| Task | Tool |
| --- | --- |
| Predict continuous value (price, temperature) | Regression |
| Predict category (yes/no, A/B/C) | Classification |
| Prevent overfitting | Regularization (Ridge, Lasso) |
| Compare models fairly | Cross-validation |
| Features on different scales | StandardScaler or MinMaxScaler |
| Check model generalization | Train/test split |
| Diagnose over/underfitting | Learning curves |

---

## 🔥 Typical ML Workflow
```python
# 1. Load & Clean (Module 2 skills)
df = pd.read_csv('data.csv')
df.head(1).T
df.info()
# Handle missing values, fix types

# 2. Define X and y
X = df[['feature1', 'feature2', 'feature3']]  # Features (predictors)
y = df['target']  # Target (what we predict)

# 3. Split Data (ALWAYS BEFORE scaling/engineering)
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 4. Scale Features (fit on train, transform both)
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)  # NO fit!

# 5. Train Model
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(X_train_scaled, y_train)

# 6. Predict
y_pred = model.predict(X_test_scaled)

# 7. Evaluate
from sklearn.metrics import mean_squared_error, r2_score
print(f"R²: {r2_score(y_test, y_pred):.4f}")
print(f"RMSE: {np.sqrt(mean_squared_error(y_test, y_pred)):.4f}")

# 8. Cross-Validate (more robust evaluation)
from sklearn.model_selection import cross_val_score
cv_scores = cross_val_score(model, X_train_scaled, y_train, cv=5, scoring='r2')
print(f"CV R²: {cv_scores.mean():.4f} (+/- {cv_scores.std():.4f})")
```

---

## 🎯 TIER 1: Must Be Automatic

### Train/Test Split
```python
from sklearn.model_selection import train_test_split

# Basic pattern
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
# Translation: "80% for training, 20% for testing, reproducible split"

# Classification with stratification (preserves class balance)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)
# Translation: "If 30% are class A in full data, 30% will be class A in both splits"

# Check split sizes
print(f"Train: {len(X_train)}, Test: {len(X_test)}")
print(f"Train %: {len(X_train) / len(X) * 100:.0f}%")

# Common test_size values:
# 0.2 (80/20) - most common
# 0.25 (75/25) - smaller datasets
# 0.3 (70/30) - very small datasets
```

---

### Scaling Workflow (CRITICAL ORDER)
```python
from sklearn.preprocessing import StandardScaler, MinMaxScaler

# MEMORIZE THIS ORDER:
# 1. Split first
# 2. Fit on train only
# 3. Transform both

# StandardScaler (z-score normalization)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)  # Fit + transform
X_test_scaled = scaler.transform(X_test)        # Transform only!
# Translation: "Learn mean/std from train, apply same transformation to test"

# MinMaxScaler (0-1 range)
scaler = MinMaxScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
# Translation: "Learn min/max from train, scale test using train's range"

# When to use which:
# StandardScaler → Normal-ish distributions, most algorithms
# MinMaxScaler → Bounded data, neural networks, when 0-1 range needed

# When scaling matters:
# YES: Linear/Logistic Regression, KNN, SVM, Neural Networks
# NO: Decision Trees, Random Forest (tree-based models)

# WHY this order matters:
# If you fit on ALL data → scaler "sees" test data statistics
# This is DATA LEAKAGE → inflated scores, poor real-world performance
```

---

### Model Training Pattern (Universal)
```python
# Same pattern for ALL sklearn models:
from sklearn.model_selection import train_test_split

# 1. Create model instance
model = SomeModel()

# 2. Fit on training data
model.fit(X_train, y_train)

# 3. Predict on test data
y_pred = model.predict(X_test)

# 4. Evaluate
score = some_metric(y_test, y_pred)

# Real examples:
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.tree import DecisionTreeClassifier

# Regression
lr = LinearRegression()
lr.fit(X_train, y_train)
y_pred = lr.predict(X_test)

# Classification
logreg = LogisticRegression()
logreg.fit(X_train, y_train)
y_pred = logreg.predict(X_test)

# Translation: "Every sklearn model uses .fit() to learn and .predict() to apply"
```

---

## 📊 REGRESSION

### Models
```python
from sklearn.linear_model import LinearRegression, Ridge, Lasso

# Linear Regression (no regularization)
lr = LinearRegression()
lr.fit(X_train, y_train)

# Ridge (L2 regularization - shrinks coefficients)
ridge = Ridge(alpha=1.0)  # Higher alpha = more regularization
ridge.fit(X_train, y_train)

# Lasso (L1 regularization - can zero out coefficients)
lasso = Lasso(alpha=0.1)
lasso.fit(X_train, y_train)

# When to use which:
# LinearRegression → Baseline, interpretability, no multicollinearity
# Ridge → Multicollinearity, many features, want to keep all features
# Lasso → Feature selection (zeros out useless features), sparse solutions

# Check coefficients
print("Coefficients:", model.coef_)
print("Intercept:", model.intercept_)

# Feature importance (which features matter most)
coef_df = pd.DataFrame({
    'feature': X.columns,
    'coefficient': model.coef_
}).sort_values('coefficient', key=abs, ascending=False)
print(coef_df)
```

---

### Regression Metrics
```python
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import numpy as np

y_pred = model.predict(X_test)

# R² (Coefficient of Determination)
r2 = r2_score(y_test, y_pred)
# Translation: "What % of variance does model explain?"
# Range: -∞ to 1.0 (1.0 = perfect, 0 = predicts mean, negative = worse than mean)

# MAE (Mean Absolute Error)
mae = mean_absolute_error(y_test, y_pred)
# Translation: "Average prediction is off by $X"
# In original units, easy to interpret

# RMSE (Root Mean Squared Error)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
# Translation: "Typical prediction error, penalizes large errors more"
# In original units, sensitive to outliers

# Print all metrics
print(f"R²: {r2:.4f}")
print(f"MAE: ${mae:,.2f}")
print(f"RMSE: ${rmse:,.2f}")

# Quick interpretation:
# R² = 0.75 → "Model explains 75% of price variation"
# MAE = $15,000 → "Predictions typically off by $15K"
# RMSE = $20,000 → "Typical error ~$20K, with some larger errors"

# MAE vs RMSE:
# MAE = $100, RMSE = $100 → Errors are consistent
# MAE = $100, RMSE = $200 → Some predictions have large errors (outliers)
```

---

### Residual Analysis
```python
import matplotlib.pyplot as plt

# Calculate residuals
residuals = y_test - y_pred

# Residual plot (predicted vs residuals)
plt.figure(figsize=(10, 6))
plt.scatter(y_pred, residuals, alpha=0.5)
plt.axhline(y=0, color='red', linestyle='--')
plt.xlabel('Predicted Values')
plt.ylabel('Residuals')
plt.title('Residual Plot')
plt.savefig('visuals/residual_plot.png', dpi=300, bbox_inches='tight')
plt.show()

# What to look for:
# ✓ Random scatter around 0 = good (assumptions met)
# ✗ Pattern/curve = nonlinear relationship (try polynomial features)
# ✗ Funnel shape = heteroscedasticity (variance changes with prediction)
# ✗ Clusters = missing categorical variable

# Histogram of residuals
plt.figure(figsize=(10, 6))
plt.hist(residuals, bins=30, edgecolor='black')
plt.axvline(x=0, color='red', linestyle='--')
plt.xlabel('Residuals')
plt.ylabel('Frequency')
plt.title('Distribution of Residuals')
plt.show()

# What to look for:
# ✓ Bell-shaped, centered at 0 = good
# ✗ Skewed = model systematically over/under predicts
```

---

## 📊 CLASSIFICATION

### Models
```python
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier

# Logistic Regression
logreg = LogisticRegression(random_state=42)
logreg.fit(X_train, y_train)
y_pred = logreg.predict(X_test)

# Decision Tree
tree = DecisionTreeClassifier(max_depth=5, random_state=42)
tree.fit(X_train, y_train)
y_pred = tree.predict(X_test)

# Get probability predictions (for ROC curves, threshold tuning)
y_proba = logreg.predict_proba(X_test)[:, 1]  # Probability of class 1
# Translation: "How confident is model that this is class 1?"

# When to use which:
# LogisticRegression → Linear decision boundary, interpretable, good baseline
# DecisionTree → Non-linear, feature importance, explainable rules
#   - Prone to overfitting without max_depth limit!
```

---

### Confusion Matrix
```python
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay

# Create confusion matrix
cm = confusion_matrix(y_test, y_pred)
print(cm)

# Visual display
plt.figure(figsize=(8, 6))
ConfusionMatrixDisplay(cm, display_labels=['Negative', 'Positive']).plot()
plt.title('Confusion Matrix')
plt.savefig('visuals/confusion_matrix.png', dpi=300, bbox_inches='tight')
plt.show()

# Understanding the matrix:
#                 Predicted
#              Neg    Pos
# Actual Neg [ TN  |  FP ]  ← Actual negatives
# Actual Pos [ FN  |  TP ]  ← Actual positives

# TN (True Negative): Correctly predicted negative
# FP (False Positive): Predicted positive, was negative (Type I error)
# FN (False Negative): Predicted negative, was positive (Type II error)
# TP (True Positive): Correctly predicted positive

# Extract values
tn, fp, fn, tp = cm.ravel()
print(f"TN: {tn}, FP: {fp}, FN: {fn}, TP: {tp}")
```

---

### Classification Metrics
```python
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.metrics import classification_report

y_pred = model.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, y_pred)
# Translation: "What % of all predictions were correct?"
# Misleading with imbalanced classes!

# Precision
precision = precision_score(y_test, y_pred)
# Translation: "Of predicted positives, what % were actually positive?"
# High precision = few false alarms
# Prioritize when: False positives are costly (spam filter, fraud alerts)

# Recall (Sensitivity)
recall = recall_score(y_test, y_pred)
# Translation: "Of actual positives, what % did we catch?"
# High recall = few missed cases
# Prioritize when: False negatives are costly (disease detection, security threats)

# F1 Score
f1 = f1_score(y_test, y_pred)
# Translation: "Harmonic mean of precision and recall"
# Use when: Need balance between precision and recall

# All at once
print(classification_report(y_test, y_pred))

# Quick interpretation example (disease screening):
# Precision = 0.90 → "90% of positive predictions actually have disease"
# Recall = 0.70 → "We catch 70% of actual disease cases"
# → High precision, lower recall = conservative (few false alarms, but miss some cases)

# METRIC SELECTION GUIDE:
# Balanced classes, care about overall performance → Accuracy
# Imbalanced classes → F1, Precision, or Recall (NOT accuracy)
# False positives are costly → Precision
# False negatives are costly → Recall
# Need balance → F1
```

---

### Handling Inverted Encodings
```python
# Problem: Sometimes target encoding is counterintuitive
# Example: disease=0, healthy=1 (opposite of what you'd expect)

# Check your encoding FIRST
print(y.value_counts())
print("What does 0 mean? What does 1 mean?")

# Option 1: Use pos_label parameter
from sklearn.metrics import precision_score, recall_score, f1_score

# If disease=0 and you want metrics about detecting disease:
precision = precision_score(y_test, y_pred, pos_label=0)
recall = recall_score(y_test, y_pred, pos_label=0)
f1 = f1_score(y_test, y_pred, pos_label=0)
# Translation: "Treat 0 as the 'positive' class for metrics"

# Option 2: Flip the encoding before analysis
# y_flipped = 1 - y  # 0 becomes 1, 1 becomes 0

# Key insight: Always know what your classes mean before interpreting metrics!
```

---

## 🔄 Cross-Validation
```python
from sklearn.model_selection import cross_val_score

# Basic cross-validation
cv_scores = cross_val_score(model, X_train, y_train, cv=5, scoring='r2')
# Translation: "Split into 5 folds, train on 4, test on 1, rotate through all"

print(f"CV Scores: {cv_scores}")
print(f"Mean: {cv_scores.mean():.4f}")
print(f"Std: {cv_scores.std():.4f}")

# Common scoring options:
# Regression: 'r2', 'neg_mean_squared_error', 'neg_mean_absolute_error'
# Classification: 'accuracy', 'precision', 'recall', 'f1'

# Why cross-validation?
# - More robust than single train/test split
# - Uses all data for both training and testing
# - Gives confidence interval (mean ± std)

# Interpretation:
# CV R² = 0.72 ± 0.05 → "Model explains ~72% of variance, consistent across folds"
# CV R² = 0.72 ± 0.20 → "High variance across folds, unstable model"

# Cross-validation for model comparison
from sklearn.linear_model import LinearRegression, Ridge, Lasso

models = {
    'LinearRegression': LinearRegression(),
    'Ridge': Ridge(alpha=1.0),
    'Lasso': Lasso(alpha=0.1)
}

for name, model in models.items():
    scores = cross_val_score(model, X_train, y_train, cv=5, scoring='r2')
    print(f"{name}: {scores.mean():.4f} (+/- {scores.std():.4f})")
```

---

## 📈 Overfitting vs Underfitting

### Diagnosis
```python
# Train on training data
model.fit(X_train, y_train)

# Score on both sets
train_score = model.score(X_train, y_train)
test_score = model.score(X_test, y_test)

print(f"Train R²: {train_score:.4f}")
print(f"Test R²: {test_score:.4f}")
print(f"Gap: {train_score - test_score:.4f}")

# DIAGNOSIS GUIDE:
# ┌─────────────────────────────────────────────────────────────┐
# │ Train: 0.95, Test: 0.60 → OVERFITTING (high variance)       │
# │ Gap is large, model memorized training data                  │
# │ Fix: More data, regularization, simpler model, fewer features│
# ├─────────────────────────────────────────────────────────────┤
# │ Train: 0.50, Test: 0.48 → UNDERFITTING (high bias)          │
# │ Both scores low, model too simple                            │
# │ Fix: More features, complex model, polynomial features       │
# ├─────────────────────────────────────────────────────────────┤
# │ Train: 0.75, Test: 0.72 → GOOD FIT                          │
# │ Small gap, acceptable scores                                 │
# │ Model generalizes well                                       │
# └─────────────────────────────────────────────────────────────┘
```

---

### Learning Curves
```python
from sklearn.model_selection import learning_curve
import numpy as np
import matplotlib.pyplot as plt

# Generate learning curve data
train_sizes, train_scores, test_scores = learning_curve(
    model, X_train, y_train,
    train_sizes=np.linspace(0.1, 1.0, 10),
    cv=5,
    scoring='r2'
)

# Calculate means and standard deviations
train_mean = train_scores.mean(axis=1)
train_std = train_scores.std(axis=1)
test_mean = test_scores.mean(axis=1)
test_std = test_scores.std(axis=1)

# Plot
plt.figure(figsize=(10, 6))
plt.plot(train_sizes, train_mean, label='Training score')
plt.plot(train_sizes, test_mean, label='Cross-validation score')
plt.fill_between(train_sizes, train_mean - train_std, train_mean + train_std, alpha=0.1)
plt.fill_between(train_sizes, test_mean - test_std, test_mean + test_std, alpha=0.1)
plt.xlabel('Training Set Size')
plt.ylabel('Score')
plt.title('Learning Curves')
plt.legend()
plt.savefig('visuals/learning_curves.png', dpi=300, bbox_inches='tight')
plt.show()

# INTERPRETATION:
# Lines converge at high score → Good model, enough data
# Lines converge at low score → Underfitting (need better features/model)
# Large gap that doesn't close → Overfitting (need more data or regularization)
# Lines still diverging at end → More data might help
```

---

## 🔧 Feature Engineering

### Common Patterns
```python
# Ratio features
df['price_per_sqft'] = df['price'] / df['sqft']
df['rooms_per_person'] = df['total_rooms'] / df['population']
df['bedroom_ratio'] = df['bedrooms'] / df['total_rooms']

# Interaction features
df['size_x_quality'] = df['sqft'] * df['quality_score']
df['location_x_size'] = df['latitude'] * df['sqft']

# Polynomial features (manual)
df['sqft_squared'] = df['sqft'] ** 2

# Binning continuous to categorical
df['price_tier'] = pd.cut(df['price'], bins=[0, 100000, 300000, np.inf],
                          labels=['Low', 'Medium', 'High'])

# Log transform (for right-skewed data)
df['log_price'] = np.log1p(df['price'])  # log1p handles zeros
# Translation: "Compress large values, spread out small values"

# Binary flags
df['has_pool'] = (df['pool'] > 0).astype(int)
df['is_luxury'] = (df['price'] > df['price'].quantile(0.9)).astype(int)

# Domain-specific (real estate examples)
df['age'] = 2024 - df['year_built']
df['renovated_recently'] = (2024 - df['last_renovation'] < 10).astype(int)
```

---

### Feature Selection
```python
# Method 1: Correlation with target
correlations = df.corr()['target'].abs().sort_values(ascending=False)
print(correlations.head(10))
# Keep features with |correlation| > 0.1 (rough guideline)

# Method 2: Feature importance from tree
from sklearn.tree import DecisionTreeRegressor
tree = DecisionTreeRegressor(max_depth=5)
tree.fit(X_train, y_train)

importance_df = pd.DataFrame({
    'feature': X.columns,
    'importance': tree.feature_importances_
}).sort_values('importance', ascending=False)
print(importance_df)

# Method 3: Lasso (zeros out unimportant features)
from sklearn.linear_model import Lasso
lasso = Lasso(alpha=0.1)
lasso.fit(X_train, y_train)

# Features with non-zero coefficients
selected = X.columns[lasso.coef_ != 0].tolist()
print(f"Selected {len(selected)} features: {selected}")

# Key insight: Not all engineered features help!
# Track baseline vs each feature, remove unhelpful ones
```

---

## 🔗 Pipelines
```python
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import Ridge

# Create pipeline
pipe = Pipeline([
    ('scaler', StandardScaler()),
    ('model', Ridge(alpha=1.0))
])

# Use like a regular model
pipe.fit(X_train, y_train)
y_pred = pipe.predict(X_test)
score = pipe.score(X_test, y_test)

# Cross-validate the whole pipeline
from sklearn.model_selection import cross_val_score
cv_scores = cross_val_score(pipe, X_train, y_train, cv=5)

# Why pipelines?
# - Prevents data leakage (scaler fitted inside CV folds)
# - Cleaner code
# - Easier deployment

# Access components
pipe.named_steps['scaler']
pipe.named_steps['model'].coef_
```

---

## 🛠️ Hyperparameter Tuning
```python
from sklearn.model_selection import GridSearchCV

# Define parameter grid
param_grid = {
    'alpha': [0.01, 0.1, 1.0, 10.0, 100.0]
}

# Grid search
grid = GridSearchCV(
    Ridge(),
    param_grid,
    cv=5,
    scoring='r2',
    return_train_score=True
)

grid.fit(X_train, y_train)

# Results
print(f"Best params: {grid.best_params_}")
print(f"Best score: {grid.best_score_:.4f}")

# Use best model
best_model = grid.best_estimator_
y_pred = best_model.predict(X_test)

# View all results
results_df = pd.DataFrame(grid.cv_results_)
print(results_df[['param_alpha', 'mean_test_score', 'std_test_score']])

# Tips:
# Start with coarse grid (few values, wide range)
# Refine around best value
# Too many params × too many values = slow!
```

---

## ⚠️ Common Gotchas

### Data Leakage
```python
# ❌ WRONG: Scale before split
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)  # Scaler sees ALL data
X_train, X_test = train_test_split(X_scaled, ...)  # Leakage!

# ✓ RIGHT: Split then scale
X_train, X_test = train_test_split(X, ...)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)  # Fit on train only
X_test_scaled = scaler.transform(X_test)  # Transform test
```

### Forgetting to Scale Test Data
```python
# ❌ WRONG: Only scale training
X_train_scaled = scaler.fit_transform(X_train)
y_pred = model.predict(X_test)  # X_test not scaled!

# ✓ RIGHT: Scale both
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
y_pred = model.predict(X_test_scaled)
```

### Using fit_transform on Test Data
```python
# ❌ WRONG: fit_transform on test
X_test_scaled = scaler.fit_transform(X_test)  # Learns new params!

# ✓ RIGHT: transform only on test
X_test_scaled = scaler.transform(X_test)  # Uses train params
```

### Accuracy on Imbalanced Data
```python
# ❌ MISLEADING: High accuracy but useless model
# If 95% are class 0, predicting all 0s gives 95% accuracy!

# ✓ RIGHT: Check class balance first
print(y.value_counts(normalize=True))

# Use appropriate metrics
from sklearn.metrics import classification_report
print(classification_report(y_test, y_pred))
# Look at precision, recall, F1 for minority class
```

### Comparing Models Without Cross-Validation
```python
# ❌ RISKY: Single split comparison
model1.fit(X_train, y_train)
model2.fit(X_train, y_train)
print(model1.score(X_test, y_test))  # Could be lucky split

# ✓ ROBUST: Cross-validation comparison
from sklearn.model_selection import cross_val_score
for model in [model1, model2]:
    scores = cross_val_score(model, X_train, y_train, cv=5)
    print(f"{type(model).__name__}: {scores.mean():.4f} ± {scores.std():.4f}")
```

---

## 📋 Quick Decision Guide

### Which Regression Model?
```
Start with LinearRegression (baseline)
    ↓
Train score >> Test score? (Overfitting)
    → Try Ridge (shrinks coefficients)
    ↓
Still overfitting or too many features?
    → Try Lasso (zeros out features)
    ↓
Need both shrinkage AND feature selection?
    → Try ElasticNet (Ridge + Lasso)
```

### Which Classification Metric?
```
Balanced classes?
    → Accuracy is fine, F1 for safety
    
Imbalanced classes?
    → NEVER trust accuracy alone
    ↓
What's more costly?
    
    False Positives costly (spam, fraud alerts)
        → Optimize Precision
        → "Only flag when very confident"
    
    False Negatives costly (disease, security)
        → Optimize Recall
        → "Catch everything, deal with false alarms"
    
    Need balance?
        → Optimize F1
```

### Do I Need Scaling?
```
Using tree-based model (DecisionTree, RandomForest, XGBoost)?
    → NO scaling needed
    
Using distance-based (KNN) or gradient-based (Linear, Logistic, SVM)?
    → YES, scale features
    
Features already on same scale?
    → Probably fine without, but scaling won't hurt
```

---

## 📚 Import Reference
```python
# Data
import pandas as pd
import numpy as np

# Visualization
import matplotlib.pyplot as plt

# Train/Test Split
from sklearn.model_selection import train_test_split

# Scaling
from sklearn.preprocessing import StandardScaler, MinMaxScaler

# Regression Models
from sklearn.linear_model import LinearRegression, Ridge, Lasso

# Classification Models
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier

# Metrics - Regression
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

# Metrics - Classification
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay, classification_report

# Cross-Validation
from sklearn.model_selection import cross_val_score, learning_curve, GridSearchCV

# Pipelines
from sklearn.pipeline import Pipeline
```

---

**Last Updated:** January 3, 2026
**Module:** 3 - Supervised Learning Foundations
**Status:** Reference document for ongoing use