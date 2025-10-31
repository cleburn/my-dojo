# EDA & Statistics Cheat Sheet

---

## Table of Contents
1. [TIER 1: Thorough Working Knowledge](#tier-1-thorough-working-knowledge)
   - [groupby()](#groupby---split-apply-combine)
   - [describe()](#describe---statistical-summary)
   - [sort_values()](#sort_values---sort-dataframe)
   - [sns.scatterplot()](#snsscatterplot---visualize-relationships)
   - [Confidence Interval Formula](#confidence-interval-formula)
2. [TIER 2: Conceptual Understanding](#tier-2-conceptual-understanding)
   - [Skewness](#skewness)
   - [Variance vs Standard Deviation](#variance-vs-standard-deviation)
   - [Regression Line Interpretation](#regression-line-interpretation)
3. [TIER 3: Awareness Level](#tier-3-awareness-level)
   - [Sampling Distributions](#sampling-distributions)
   - [t-Critical Values](#t-critical-values)
   - [Trimmed Means](#trimmed-means)
4. [Typical EDA Workflow](#typical-eda-workflow)
5. [Quick Reference: When to Use What](#quick-reference-when-to-use-what)
6. [Real Estate Project Applications](#real-estate-project-applications)

---

## TIER 1: Thorough Working Knowledge

### `groupby()` - Split-Apply-Combine
```python
# Basic pattern
df.groupby('category')['value'].aggregation()

# Examples
df.groupby('neighborhood')['price'].mean()
df.groupby(['city', 'type'])['price'].agg(['mean', 'median', 'count'])

# Common aggregations: .mean(), .sum(), .count(), .median(), .min(), .max()
```
**Use when:** "What's the average/total/count BY category?"

---

### `describe()` - Statistical Summary
```python
df.describe()              # All numeric columns
df['price'].describe()     # Single column
```
**Returns:** count, mean, std, min, 25%, 50% (median), 75%, max

**Always check:** 
- Mean vs Median (50%) → If far apart, data is skewed
- Min/Max vs 75%/25% → Spot outliers

---

### `sort_values()` - Sort DataFrame
```python
df.sort_values('price')                              # Ascending (default)
df.sort_values('price', ascending=False)              # Descending
df.sort_values(['city', 'price'], ascending=[True, False])  # Multiple columns
```
**Use when:** Finding top/bottom performers, creating ranked lists

---

### `sns.scatterplot()` - Visualize Relationships
```python
sns.scatterplot(data=df, x='sqft', y='price')
sns.scatterplot(data=df, x='sqft', y='price', hue='neighborhood')  # Add color
sns.scatterplot(data=df, x='sqft', y='price', size='bedrooms')     # Add size
```
**Look for:**
- Positive correlation: Points go up-right
- Negative correlation: Points go down-right
- No correlation: Random cloud
- Outliers: Points far from cluster

---

### Confidence Interval Formula
```
CI = x̄ ± (t * (s / √n))

x̄ = sample mean
t = t-critical value (depends on confidence level & sample size)
s = sample standard deviation
n = sample size
```

**In Python:**
```python
from scipy import stats
import numpy as np

mean = df['price'].mean()
std = df['price'].std()
n = len(df['price'])
confidence = 0.95

# Get t-critical value
t_crit = stats.t.ppf((1 + confidence) / 2, n - 1)

# Calculate margin of error
margin = t_crit * (std / np.sqrt(n))

# Confidence interval
lower = mean - margin
upper = mean + margin

print(f"95% CI: [{lower:.2f}, {upper:.2f}]")
```

**Translation:** "We're 95% confident the true population mean is between lower and upper"

---

## TIER 2: Conceptual Understanding

### Skewness
- **Right-skewed (positive):** Mean > Median. Long tail on right.
  - Example: Income, home prices (most average, few very high)
- **Left-skewed (negative):** Mean < Median. Long tail on left.
  - Example: Age at retirement (most retire 62-67, few at 40)
- **Symmetric:** Mean ≈ Median. Bell curve.

**Why it matters:** 
- Skewed data → Use median instead of mean for "typical" value
- May need log transformation for modeling

**Quick check:** Compare mean vs median in `.describe()`

---

### Variance vs Standard Deviation
- **Variance (σ²):** Average of squared differences from mean
  - Units are squared (hard to interpret)
- **Standard Deviation (σ):** Square root of variance
  - Same units as data (easy to interpret)

**Rule of thumb:**
- ~68% of data within 1 std dev of mean
- ~95% within 2 std devs
- ~99.7% within 3 std devs

**Example:** Average price $300K, std dev $50K → Most homes $250K-$350K

---

### Regression Line Interpretation
**Equation:** `y = mx + b`
- **m (slope):** For every 1-unit increase in x, y changes by m units
- **b (intercept):** Value of y when x = 0

**Example:** `price = 150 * sqft + 50000`
- Each sqft adds $150 to price
- Base price (0 sqft) is $50K

**R² (R-squared):** How well line fits (0 to 1)
- R² = 0.80 → "80% of price variation explained by sqft"

---

## TIER 3: Awareness Level

### Sampling Distributions
Taking many samples → calculating mean of each → those means form a distribution.
**Foundation of:** Confidence intervals, hypothesis testing, A/B tests

---

### t-Critical Values
Multiplier in confidence intervals. Depends on:
1. Confidence level (90%, 95%, 99%)
2. Sample size (degrees of freedom)

**Get it:** `scipy.stats.t.ppf((1 + confidence) / 2, df=n-1)`

---

### Trimmed Means
Mean after removing % of extreme values from both ends.
**Use:** Reduce outlier influence without removing all data

**In Python:** `scipy.stats.trim_mean(data, proportiontocut=0.1)`

---

## Typical EDA Workflow

1. **Load data**
   ```python
   df = pd.read_csv('data.csv')
   df.head()
   df.info()
   ```

2. **Statistical summary** → Spot skewness, outliers, range
   ```python
   df.describe()
   ```

3. **Group comparisons** → Compare categories
   ```python
   df.groupby('category')['value'].mean()
   ```

4. **Sort for insights** → Top/bottom performers
   ```python
   df.sort_values('value', ascending=False).head(10)
   ```

5. **Visualize relationships** → Scatterplots for correlations
   ```python
   sns.scatterplot(data=df, x='feature', y='target')
   ```

6. **Calculate confidence intervals** → Quantify uncertainty
   ```python
   # See CI formula above
   ```

7. **Check skewness** → Decide mean vs median
   ```python
   # Compare mean vs median from .describe()
   ```

---

## Quick Reference: When to Use What

| Task | Tool |
|------|------|
| First look at data | `.head()`, `.info()`, `.describe()` |
| Compare categories | `.groupby()` |
| Find top/bottom | `.sort_values()` + `.head()` |
| Spot relationships | `sns.scatterplot()` |
| Quantify uncertainty | Confidence intervals |
| Handle outliers | Check skewness, consider trimmed mean |
| Predictive relationship | Regression line + R² |

---

## Real Estate Project Applications

### "Which neighborhoods have highest occupancy?"
```python
df.groupby('neighborhood')['occupancy_rate'].mean().sort_values(ascending=False)
```

### "Seasonal price trends?"
```python
df.groupby('month')['price'].mean()
sns.lineplot(data=df, x='month', y='price')
```

### "Revenue drivers?"
```python
sns.scatterplot(data=df, x='reviews', y='revenue')
sns.scatterplot(data=df, x='price', y='revenue')
```

### "What's the typical price? (handling skewness)"
```python
mean = df['price'].mean()
median = df['price'].median()
if abs(mean - median) > median * 0.1:  # More than 10% difference
    print(f"Data is skewed. Use median: ${median:.2f}")
else:
    print(f"Data is symmetric. Use mean: ${mean:.2f}")
```

---

## Remember
- **Run `.describe()` first** → Your data compass
- **Mean vs Median** → Quick skewness check
- **groupby() + aggregation** → Most common pattern
- **Visualize before modeling** → Scatterplots reveal relationships
- **Confidence intervals** → Quantify uncertainty in estimates