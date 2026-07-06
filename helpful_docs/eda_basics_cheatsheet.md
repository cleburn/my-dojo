### When to Use What

| Task | Tool |
| --- | --- |
| First look at data | `.head()`, `.info()`, `.describe()` |
| Compare categories | `.groupby()` |
| Find top/bottom | `.sort_values()` + `.head()` |
| Spot relationships | `sns.scatterplot()` or `plt.scatter()` |
| Compare distributions | Histograms, boxplots |
| Quantify uncertainty | Confidence intervals |
| Test differences | t-tests |
| Handle outliers | Check skewness, use median |

---

## 🔥 Typical EDA Workflow

```python
# 1. Load & Inspect
df = pd.read_csv('data.csv')
df.head(1).T  # Transposed view - see all columns
df.info()
df.describe()

# 2. Clean Data (ALWAYS FIRST)
df['price'] = df['price'].str.replace(r'[$,]', '', regex=True).astype(float)
df['zipcode'] = df['zipcode'].astype(str)
df.dropna(subset=['critical_column'])

# 3. Explore Patterns
df.groupby('category')['value'].mean()
df.sort_values('value', ascending=False).head(10)

# 4. Visualize
plt.hist(df['column'], bins=50)
sns.scatterplot(data=df, x='feature', y='target')

# 5. Test Hypotheses
from scipy import stats
group1 = df[df['category'] == 'A']['value']
group2 = df[df['category'] == 'B']['value']
statistic, p_value = stats.ttest_ind(group1, group2)

# 6. Calculate Confidence Intervals (when needed)
from scipy import stats
import numpy as np
mean = df['price'].mean()
std = df['price'].std()
n = len(df['price'])
confidence = 0.95
t_crit = stats.t.ppf((1 + confidence) / 2, n - 1)
margin = t_crit * (std / np.sqrt(n))
ci_lower = mean - margin
ci_upper = mean + margin
print(f"95% CI: [{ci_lower:.2f}, {ci_upper:.2f}]")

```

---

## 🎯 TIER 1: Must Be Automatic

### Viewing Data

```python
# See all columns at once
df.head(1).T  # BEST - transposed view
df.columns.tolist()  # Just column names as list
list(df.columns)  # Alternative

# See columns + types
df.dtypes
df.info()

# Show all columns/rows (override truncation)
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
df.head()

# Reset to default
pd.set_option('display.max_columns', 10)

```

---

### Filtering & Selecting

```python
# Basic patterns
df[df['column'] > value]  # Single condition
df[(df['col1'] > value) & (df['col2'] < value)]  # AND
df[(df['col1'] > value) | (df['col2'] < value)]  # OR
df[['col1', 'col2', 'col3']]  # Select columns

# Combined filter + select
df[df['price'] > 100][['name', 'price', 'neighborhood']]

# Find max/min rows
df[df['column'] == df['column'].max()]
df[df['column'] == df['column'].min()]

# Count rows matching condition
len(df[df['column'] > value])
df[df['column'] > value].shape[0]

# Filter by percentile
threshold = df['column'].quantile(0.90)  # Top 10%
top_10 = df[df['column'] >= threshold]

# Multiple conditionals
# Basic pattern
df[(condition1) & (condition2)]  # AND - both must be true
df[(condition1) | (condition2)]  # OR - either can be true

# Real estate example - AND
df[(df['price'] > 200000) & (df['bedrooms'] >= 3)]
# Translation: "Houses over $200K AND at least 3 bedrooms"

# Real estate example - OR
df[(df['neighborhood'] == 'Downtown') | (df['neighborhood'] == 'Westlake')]
# Translation: "Houses in Downtown OR Westlake"

# Combining AND + OR
df[(df['price'] < 300000) & ((df['bedrooms'] >= 3) | (df['bathrooms'] >= 2))]
# Translation: "Under $300K AND (3+ bedrooms OR 2+ bathrooms)"

# Greater than and less than
df[(df['age'] > 18) & (df['age'] < 65)]

# Multiple categories
df[(df['city'] == 'Austin') & (df['property_type'] == 'Condo')]

# Not equal
df[(df['status'] != 'Sold') & (df['price'] > 500000)]

# COMMON GOTCHAS:
# - Use & for AND, | for OR (not "and"/"or")
# - Multiple conditions need parentheses: (cond1) & (cond2)
# - Double brackets for multiple columns: df[['col1', 'col2']]

```

---

### Creating Calculated Columns

```python
# Basic pattern
df['new_column'] = calculation

# Examples
df['price_per_sqft'] = df['price'] / df['sqft']
df['total_revenue'] = df['price'] * df['occupancy']
df['is_expensive'] = df['price'] > 200  # Boolean
df['year_month'] = df['year'].astype(str) + '-' + df['month'].astype(str)

# New Columns with conditional value returns
df['new_column'] = np.where(condition, value_if_true, value_if_false)

# Real estate example
import numpy as np
df['income_category'] = np.where(df['MedInc'] > df['MedInc'].median(), 'High', 'Low')
# Translation: "For each row, if MedInc is above the median, assign 'High', otherwise 'Low'"

# Alternative using .apply() + lambda (slower but readable)
df['income_category'] = df['MedInc'].apply(lambda x: 'High' if x > df['MedInc'].median() else 'Low')

# When to use:
# np.where() → Fast, simple binary conditions
# .apply() → More complex logic or multiple conditions

# Check distribution
df['income_category'].value_counts()

```

---

### loc/iloc

```python
# iloc = Integer Location (position-based)
df.iloc[0]          # First row
df.iloc[0:5]        # Rows 0-4
df.iloc[0, 2]       # Row 0, column 2

# loc = Label Location (name-based)
df.loc[0]                           # Row with index label 0
df.loc[0:5, 'salary']              # Rows 0-5, salary column
df.loc[df['salary'] > 50000, ['name', 'salary']]  # Filter + select in one step

# Translation:
# iloc = "Give me row/column by NUMBER"
# loc = "Give me row/column by NAME"

# When to use which:
# iloc → slicing by position, don't care about labels
# loc → filtering with conditions, selecting named columns
```

---

### Sorting

```python
# Basic pattern
df.sort_values('column', ascending=False)  # Descending (high to low)
df.sort_values('column', ascending=True)   # Ascending (low to high)
df.sort_values('column')  # Default is ascending

# Multiple columns (tiebreakers)
df.sort_values(['neighborhood', 'price'], ascending=[True, False])
# Translation: "Sort by neighborhood A-Z, then within each neighborhood sort price high to low"

# Sort and display top N
df.sort_values('price', ascending=False).head(10)

```

---

### Groupby & Aggregation

```python
# Basic pattern
df.groupby('column')['target'].aggregation_function()

# Single aggregation
df.groupby('neighborhood')['price'].mean()
df.groupby('neighborhood')['listing_url'].nunique()

# Multiple columns groupby
df.groupby(['city', 'property_type'])['price'].mean()

# Common aggregations
.mean()    # Average
.median()  # Middle value
.sum()     # Total
.count()   # Count rows
.nunique() # Count unique values
.min()     # Minimum
.max()     # Maximum
```

---

### Filter → Groupby → Sort (Common Pattern)

```python
# Basic pattern
df[filter].groupby('category')['target'].agg().sort_values(ascending=False)

# Real example
df[df['price'] < 1000].groupby('neighborhood')['listing_url'].nunique().sort_values(ascending=False).head(10)
# Translation: "Filter price < 1000, then count unique listings per neighborhood, sort high to low, show top 10"

# Multi-line format (same thing, more readable)
(df[df['price'] < 1000]
   .groupby('neighborhood')['listing_url']
   .nunique()
   .sort_values(ascending=False)
   .head(10)
)
```

---

### Multiple Aggregations (IMPORTANT - NEW)

### Simple Version: One Function Per Column

```python
# Basic pattern
df.groupby('category').agg({
    'col1': 'function1',
    'col2': 'function2'
})

# Real example
df[df['price'] < 750].groupby('neighborhood').agg({
    'listing_url': 'nunique',
    'price': 'median'
}).rename(columns={
    'listing_url': 'unique_listings',
    'price': 'median_price'
}).sort_values('unique_listings', ascending=False).head(10)
# Translation: "Count unique listings + median price per neighborhood, rename columns, sort by count"

# Common price aggregations
'price': 'mean'      # Average
'price': 'median'    # Median (better with outliers)
'price': 'min'       # Minimum
'price': 'max'       # Maximum

```

---

### Advanced: Multiple Functions Per Column (Creates MultiIndex)

```python
# STEP 1: See the MultiIndex problem
result = df[df['price'] < 700].groupby('neighborhood').agg({
    'listing_url': 'nunique',
    'price': ['mean', 'median']  # Multiple functions = MultiIndex columns
})
print(result.columns)
# Output: MultiIndex([('listing_url', 'nunique'), ('price', 'mean'), ('price', 'median')])

# STEP 2: Flatten MultiIndex columns
result.columns = ['_'.join(col) for col in result.columns]
print(result.columns)
# Output: Index(['listing_url_nunique', 'price_mean', 'price_median'])

# STEP 3: Rename and sort
result = result.rename(columns={
    'listing_url_nunique': 'unique_listings',
    'price_mean': 'avg_price',
    'price_median': 'median_price'
})
result.sort_values('unique_listings', ascending=False).head(5)

# Or Rename directly in the aggregation
results1_df = df.groupby('Category').agg(
    purchase_count=('column name', 'count'),
    mean_purchase_amount=('column name','mean'),
    median_purchase_amount=('column name','median')
).sort_values(
    by='mean_purchase_amount',
    ascending=False
).head(10)

print(results1_df)

# ALL-IN-ONE VERSION (using .pipe)
(df[df['price'] < 700]
    .groupby('neighborhood')
    .agg({'listing_url': 'nunique', 'price': ['mean', 'median']})
    .pipe(lambda x: x.set_axis(['_'.join(col) for col in x.columns], axis=1))
    .rename(columns={
        'listing_url_nunique': 'unique_listings',
        'price_mean': 'avg_price',
        'price_median': 'median_price'
    })
    .sort_values('unique_listings', ascending=False)
    .head(5)
)
# Translation: "Aggregate multiple stats, flatten MultiIndex, rename columns, sort, display top 5"

```

---

### Data Cleaning

```python
# Remove currency symbols
df['price'] = df['price'].str.replace(r'[$,]', '', regex=True).astype(float)
# Translation: "Remove $ and commas, convert to float"

# Remove all non-numeric except decimal
df['price'] = df['price'].str.replace(r'[^\d.]', '', regex=True).astype(float)

# Fix data types
df['zipcode'] = df['zipcode'].astype(str)
df['price'] = df['price'].astype(float)

# Handle missing values
df.isna().sum()  # Count NaNs per column
df.dropna(subset=['critical_column'])  # Drop rows where column is NaN
df['column'].fillna(0)  # Fill NaNs with 0
df['column'].fillna(df['column'].median())  # Fill with median

# When to use each strategy:
# 1. Drop rows/columns: <5% missing, or NaN means invalid data
# 2. Fill with 0/"Unknown": Need placeholder for categorical
# 3. Fill with mean/median: Preserve distribution for numeric
# 4. Forward/backward fill: Time-series or ordered data
# 5. Leave as NaN: Missingness is meaningful information

# Example Work Flow
# Clean price column
df['price'] = df['price'].str.replace(r'[^\d.]', '', regex=True).astype(float)

# Calculate trim boundaries BEFORE filling NaNs
lower = df['price'].quantile(0.05)
upper = df['price'].quantile(0.95)

# Trim outliers (ASSIGN back to df)
df = df[(df['price'] >= lower) & (df['price'] <= upper)]

# NOW fill missing values with mean of TRIMMED data
df['price'] = df['price'].fillna(df['price'].mean())

# Verify
print(f"Rows after trimming: {len(df)}")
print(f"Price range: ${df['price'].min():.2f} - ${df['price'].max():.2f}")
print(f"Missing values: {df['price'].isna().sum()}")

```

---

### Finding Max/Min Values

```python
# Basic pattern
max_value = series.max()
series[series == max_value]

# Real example - find ALL neighborhoods tied for highest occupancy
occupancy_by_neighborhood = df.groupby('neighborhood')['occupancy'].max()
max_occupancy = occupancy_by_neighborhood.max()
occupancy_by_neighborhood[occupancy_by_neighborhood == max_occupancy]

# One-liner version
occupancy_by_neighborhood[occupancy_by_neighborhood == occupancy_by_neighborhood.max()]

```

---

## 📊 Visualizations

### Visualization Decision Tree

```python
# WHICH VIZ FOR WHICH QUESTION?
# Single variable distribution → Histogram
"What's the typical price range?" → plt.hist(df['price'])

# Compare groups → Boxplot  
"Do downtown vs suburbs differ?" → df.boxplot(column='price', by='neighborhood')

# Relationship between two → Scatter
"Does size affect price?" → plt.scatter(df['sqft'], df['price'])

# Change over time → Line plot
"How did prices trend?" → plt.plot(df['month'], df['avg_price'])
```

### Histogram

```python
import matplotlib.pyplot as plt

# Basic pattern
plt.figure(figsize=(10, 6))
plt.hist(df['column'], bins=50, edgecolor='black')
plt.axvline(df['column'].mean(), color='red', linestyle='--', label='Mean')
plt.axvline(df['column'].median(), color='green', linestyle='--', label='Median')
plt.xlabel('Column Name')
plt.ylabel('Frequency')
plt.title('Distribution of Column')
plt.legend()
plt.savefig('visuals/histogram.png', dpi=300, bbox_inches='tight')  # Save first
plt.show()  # Display second

# What to look for:
# - Mean vs Median lines far apart = skewed data
# - Long tail on right = right-skewed (use median)
# - Long tail on left = left-skewed (use median)
# - Bell shape = symmetric (mean OK)

# What a Histogram Does

Purpose: Shows distribution of a single numeric variable by grouping values into bins and counting frequency

Bins: Divides the range into intervals (e.g., $0-100, $100-200, etc.) and counts how many values fall in each

Why it matters: Reveals shape (symmetric vs skewed), central tendency (where most values cluster), and outliers (extreme values)

# How to choose bin count:
# Default (matplotlib decides): 
plt.hist(df['column'])  # Often around 10 bins
# Manual specification:
plt.hist(df['column'], bins=50)  # Usually good for 1000+ data points
# Rule of thumb:
# <100 data points: bins=10-20
# 100-1000 points: bins=20-40  
# 1000+ points: bins=40-60

# Syntax Breakdown
# Basic pattern
plt.hist(data_to_plot, bins=number, edgecolor='black')

# Real example
plt.hist(df['price'], bins=50, edgecolor='black')
# Translation: "Take the price column, divide into 50 bins, outline bars in black"

# Common parameters:
bins=50          # How many intervals (more bins = more detail, fewer = smoother)
edgecolor='black' # Outline color (makes bars easier to see)
alpha=0.7        # Transparency (0=invisible, 1=solid)
color='blue'     # Bar color

# Setting axis limits:
# Set x-axis limits to the minimum and maximum of the data
plt.xlim(data.min(), data.max())

# Selecting the Right Column
# Rule: Must be NUMERIC column (not categorical)

# Check data types first
df.dtypes

# Good histogram candidates:
df['price'].hist()           # Money values
df['sqft'].hist()            # Measurements
df['occupancy_rate'].hist()  # Percentages
df['review_count'].hist()    # Counts

# Bad histogram candidates:
df['neighborhood'].hist()    # Categorical (use bar chart instead)
df['property_type'].hist()   # Categorical
df['host_name'].hist()       # Text

# Filter Before Plotting
# Pattern 1: Filter outliers (keep values within range)
filtered_data = df[(df['price'] > lower_bound) & (df['price'] < upper_bound)]
plt.hist(filtered_data['price'], bins=50)

# Real example - remove extreme outliers
plt.hist(df[df['price'] < 1000]['price'], bins=50, edgecolor='black')
# Translation: "Only plot prices under $1000"

# Pattern 2: Use percentiles to auto-trim outliers
lower = df['price'].quantile(0.05)  # Bottom 5%
upper = df['price'].quantile(0.95)  # Top 5%
trimmed = df[(df['price'] >= lower) & (df['price'] <= upper)]
plt.hist(trimmed['price'], bins=50, edgecolor='black')
# Translation: "Plot middle 90% of data, ignore extreme 5% on each end"

# Pattern 3: Filter specific range
plt.hist(df[(df['price'] > 100) & (df['price'] < 500)]['price'], bins=30)
# Translation: "Only plot prices between $100-$500"

# Complete Example
# Step 1: Choose numeric column and filter
data = df[df['price'] < 1000]['price']

# Step 2: Create histogram
plt.figure(figsize=(10, 6))
plt.hist(data, bins=50, edgecolor='black')

# Step 3: Add mean/median lines
plt.axvline(data.mean(), color='red', linestyle='--', label='Mean')
plt.axvline(data.median(), color='green', linestyle='--', label='Median')

# Step 4: Labels
plt.xlabel('Price ($)')
plt.ylabel('Frequency')
plt.title('Distribution of Airbnb Prices (< $1000)')
plt.legend()
plt.show()

# Method 1: Create Variable First (Clearer)
# Step 1: Filter and store
filtered_data = df[df['price'] < 1000]['price']

# Step 2: Plot the variable
plt.hist(filtered_data, bins=50, edgecolor='black')
plt.axvline(filtered_data.mean(), color='red', linestyle='--', label='Mean')
plt.axvline(filtered_data.median(), color='green', linestyle='--', label='Median')

# Pros: Easier to read, can reuse filtered_data multiple times
# Cons: Extra line of code

# Method 2: Inline Filter (More Compact)
# All-in-one: filter inside plt.hist()
plt.hist(df[df['price'] < 1000]['price'], bins=50, edgecolor='black')
plt.axvline(df[df['price'] < 1000]['price'].mean(), color='red', linestyle='--', label='Mean')
plt.axvline(df[df['price'] < 1000]['price'].median(), color='green', linestyle='--', label='Median')

# Pros: Fewer lines
# Cons: Repetitive (filter applied 3 times), harder to read

# Best Practice: Hybrid Approach
# Filter once, use multiple times
data = df[df['price'] < 1000]['price']

plt.figure(figsize=(10, 6))
plt.hist(data, bins=50, edgecolor='black')
plt.axvline(data.mean(), color='red', linestyle='--', label='Mean')
plt.axvline(data.median(), color='green', linestyle='--', label='Median')
plt.xlabel('Price ($)')
plt.ylabel('Frequency')
plt.title('Distribution of Airbnb Prices (< $1000)')
plt.legend()
plt.show()

# Why this is best:
# - Filter applied once (efficient)
# - Code is readable
# - Easy to calculate stats (mean, median) on same filtered data

When to Use Each
Use variable approach when:

You need to calculate stats (mean, median, std) on the filtered data
You'll reference the filtered data multiple times
Code readability matters (clearer what you're plotting)

Use inline approach when:

Very simple, one-time plot
No additional calculations needed
Quick exploratory visualization

General rule: If you type the same filter more than once, create a variable instead.
```

---

### Boxplot

```python
### Boxplot

**Core concept:** Compare a NUMERIC variable across CATEGORIES. Shows distribution differences between groups.

---

#### Method 1: Pandas Built-in (Easiest - Use When You Want ALL Categories)

# Basic pattern
plt.figure(figsize=(10, 6))
df.boxplot(column='numeric_column', by='category_column')
plt.suptitle('')  # Remove default title
plt.title('Your Title')
plt.xlabel('Category')
plt.ylabel('Values')
plt.savefig('visuals/boxplot.png', dpi=300, bbox_inches='tight')
plt.show()

# Real example - Wine quality
plt.figure(figsize=(10, 6))
df.boxplot(column='alcohol', by='quality')
plt.suptitle('')
plt.title('Alcohol Content by Quality Score')
plt.xlabel('Quality Score')
plt.ylabel('Alcohol (%)')
plt.show()
# Translation: "Show alcohol distribution for EACH quality score (3, 4, 5, 6, 7, 8)"
# Result: 6 boxes, one per quality level

---

#### Method 2: Manual plt.boxplot (More Control - Use When Comparing SPECIFIC Groups)

# Basic pattern - understanding the filter
df[df['category'] == value]['numeric_column']
# Step 1: df['category'] == value  → True/False for each row
# Step 2: df[filter]                → Keep only True rows
# Step 3: ['numeric_column']        → Extract that column

# Complete pattern
plt.figure(figsize=(10, 6))
plt.boxplot([df[df['category'] == 'Group1']['value'],
             df[df['category'] == 'Group2']['value'],
             df[df['category'] == 'Group3']['value']],
            labels=['Group1', 'Group2', 'Group3'])
plt.xlabel('Category')
plt.ylabel('Values')
plt.title('Title')
plt.show()

# Real example - Compare only quality 5 vs 8 (skip middle scores)
quality_5 = df[df['quality'] == 5]['alcohol']
quality_8 = df[df['quality'] == 8]['alcohol']

plt.figure(figsize=(10, 6))
plt.boxplot([quality_5, quality_8],
            labels=['Average Wine (5)', 'Premium Wine (8)'])
plt.xlabel('Quality Tier')
plt.ylabel('Alcohol (%)')
plt.title('Alcohol: Average vs Premium Wines')
plt.show()
# Translation: "Compare alcohol content for ONLY quality 5 and 8"
# Why: Focus on extremes, ignore middle

---

#### Step-by-Step Example

# Question: "Does volatile acidity differ for low, medium, high quality wines?"

# STEP 1: Extract each group's data
low_quality = df[df['quality'] <= 4]['volatile acidity']
med_quality = df[(df['quality'] == 5) | (df['quality'] == 6)]['volatile acidity']
high_quality = df[df['quality'] >= 7]['volatile acidity']

# STEP 2: Check sample sizes
print(f"Low quality: {len(low_quality)} wines")
print(f"Medium quality: {len(med_quality)} wines")
print(f"High quality: {len(high_quality)} wines")

# STEP 3: Create boxplot
plt.figure(figsize=(10, 6))
plt.boxplot([low_quality, med_quality, high_quality],
            labels=['Low (≤4)', 'Medium (5-6)', 'High (≥7)'])
plt.xlabel('Quality Tier')
plt.ylabel('Volatile Acidity')
plt.title('Volatile Acidity by Quality Tier')
plt.show()

---

#### When to Use Each Method

**Use pandas built-in (Method 1) when:**
- You have a category column already
- You want ALL categories shown
- Quick exploration

**Use manual plt.boxplot (Method 2) when:**
- Comparing SPECIFIC groups only (e.g., just low vs high, skip medium)
- Need to create groups on-the-fly with custom filters
- More control over group definitions

---

#### What to Look For in Boxplots

- **Box:** Middle 50% of data (25th to 75th percentile)
- **Line in box:** Median (50th percentile)
- **Whiskers:** Typical range (extends 1.5 × IQR from box)
- **Dots beyond whiskers:** Outliers (unusually high/low values)
- **Compare across groups:**
  - Higher box = higher values for that group
  - Taller box = more spread/variability
  - No overlap = groups clearly different
  - Heavy overlap = groups similar
```

---

### Scatter Plot

```python
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

# Basic pattern
plt.figure(figsize=(10, 6))
plt.scatter(data=df, x='column1', y='column2', alpha=0.4)
plt.xlabel('X Label')
plt.ylabel('Y Label')
plt.title('Title')
plt.show()

# With formatted y-axis (thousands)
plt.figure(figsize=(10, 6))
plt.scatter(data=df, x='zipcode', y='revenue', alpha=0.4)
plt.xlabel('ZIP Codes')
plt.ylabel('Revenue')
plt.title('Revenue by Location')

# Format y-axis as $K
ax = plt.gca()
ax.yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, p: f'${x/1000:.0f}K'))
# Translation: "Divide by 1000, no decimals, add $K"

plt.savefig('visuals/scatter.png', dpi=300, bbox_inches='tight')
plt.show()

# Y-axis formatting options:
# Thousands: lambda x, p: f'${x/1000:.0f}K'
# Millions: lambda x, p: f'${x/1e6:.1f}M'
# Commas: ticker.StrMethodFormatter('${x:,.0f}')

# What to look for:
# - Upward trend = positive correlation
# - Downward trend = negative correlation
# - Random cloud = no correlation
# - Outliers = points far from cluster

# Including correlation coefficient:
corr = df['x'].corr(df['y'])
plt.text(0.05, 0.95, f'Correlation: {corr:.3f}',
         transform=plt.gca().transAxes, fontsize=12,
         bbox=dict(boxstyle='round', facecolor='wheat'))
plt.show()
```

---

### Bar Chart

```python
### Bar Chart
**Core concept:** Compare VALUES across CATEGORIES. Shows counts, totals, or averages for discrete groups.

---

#### Method 1: Pandas Built-in (Easiest - Use for Counts or Pre-Aggregated Data)

# Basic pattern - value counts (counting occurrences)
plt.figure(figsize=(10, 6))
df['category_column'].value_counts().plot(kind='bar')
plt.xlabel('Category')
plt.ylabel('Count')
plt.title('Your Title')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('visuals/bar_chart.png', dpi=300, bbox_inches='tight')
plt.show()

# Real example - Count wines by quality score
plt.figure(figsize=(10, 6))
df['quality'].value_counts().sort_index().plot(kind='bar')
plt.xlabel('Quality Score')
plt.ylabel('Number of Wines')
plt.title('Wine Count by Quality Score')
plt.xticks(rotation=0)
plt.show()
# Translation: "How many wines have each quality score?"
# Note: .sort_index() puts bars in order (3, 4, 5, 6...) instead of by count

# Basic pattern - aggregated values (mean, sum, etc.)
plt.figure(figsize=(10, 6))
df.groupby('category_column')['numeric_column'].mean().plot(kind='bar')
plt.xlabel('Category')
plt.ylabel('Average Value')
plt.title('Your Title')
plt.show()

# Real example - Average alcohol by quality
plt.figure(figsize=(10, 6))
df.groupby('quality')['alcohol'].mean().plot(kind='bar')
plt.xlabel('Quality Score')
plt.ylabel('Average Alcohol (%)')
plt.title('Average Alcohol Content by Quality')
plt.xticks(rotation=0)
plt.show()
# Translation: "What's the average alcohol for each quality score?"

---

#### Method 2: Manual plt.bar (More Control - Custom Categories or Styling)

# Basic pattern
categories = ['Group1', 'Group2', 'Group3']
values = [value1, value2, value3]

plt.figure(figsize=(10, 6))
plt.bar(categories, values)
plt.xlabel('Category')
plt.ylabel('Values')
plt.title('Title')
plt.show()

# Real example - Compare specific quality tiers
# Step 1: Calculate your values
avg_low = df[df['quality'] <= 4]['alcohol'].mean()
avg_med = df[(df['quality'] == 5) | (df['quality'] == 6)]['alcohol'].mean()
avg_high = df[df['quality'] >= 7]['alcohol'].mean()

# Step 2: Create lists
categories = ['Low (≤4)', 'Medium (5-6)', 'High (≥7)']
averages = [avg_low, avg_med, avg_high]

# Step 3: Plot
plt.figure(figsize=(10, 6))
plt.bar(categories, averages, color=['#e74c3c', '#f39c12', '#27ae60'])
plt.xlabel('Quality Tier')
plt.ylabel('Average Alcohol (%)')
plt.title('Average Alcohol by Quality Tier')
plt.show()
# Translation: "Compare average alcohol for custom-defined quality groups"

---

#### Adding Value Labels on Bars

# Pattern for adding numbers on top of bars
fig, ax = plt.subplots(figsize=(10, 6))
bars = ax.bar(categories, values)

# Add value labels
for bar, value in zip(bars, values):
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.5,
            f'{value:.1f}', ha='center', va='bottom')

plt.xlabel('Category')
plt.ylabel('Values')
plt.title('Title')
plt.show()

# Real example - Counts with labels
fig, ax = plt.subplots(figsize=(10, 6))
counts = df['quality'].value_counts().sort_index()
bars = ax.bar(counts.index.astype(str), counts.values)

for bar, count in zip(bars, counts.values):
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 10,
            str(count), ha='center', va='bottom')

plt.xlabel('Quality Score')
plt.ylabel('Number of Wines')
plt.title('Wine Count by Quality Score')
plt.show()
# Translation: "Show exact counts above each bar"

---

#### Horizontal Bar Chart (For Long Category Names)

# Basic pattern
plt.figure(figsize=(10, 6))
df['category_column'].value_counts().plot(kind='barh')
plt.xlabel('Count')
plt.ylabel('Category')
plt.title('Your Title')
plt.show()

# Real example - Neighborhoods with long names
plt.figure(figsize=(10, 8))
df['neighborhood'].value_counts().head(10).plot(kind='barh')
plt.xlabel('Number of Listings')
plt.ylabel('Neighborhood')
plt.title('Top 10 Neighborhoods by Listing Count')
plt.show()
# Translation: "Horizontal bars prevent overlapping text on y-axis"

---

#### Step-by-Step Example

# Question: "Which property types have the highest average price?"

# STEP 1: Calculate aggregated values
avg_by_type = df.groupby('property_type')['price'].mean().sort_values(ascending=False)
print(avg_by_type)

# STEP 2: Decide how many to show (top 5? all?)
top_5 = avg_by_type.head(5)

# STEP 3: Create bar chart
plt.figure(figsize=(10, 6))
top_5.plot(kind='bar', color='steelblue')
plt.xlabel('Property Type')
plt.ylabel('Average Price ($)')
plt.title('Top 5 Property Types by Average Price')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

# STEP 4: Add context (optional - sample sizes)
counts = df.groupby('property_type')['price'].count()
for prop_type in top_5.index:
    print(f"{prop_type}: ${top_5[prop_type]:,.0f} (n={counts[prop_type]})")

---

#### Logistic Regression

# Basic pattern - get class counts
y_train.value_counts()

# Real example - visualize distribution
import matplotlib.pyplot as plt

# Get counts
train_counts = y_train.value_counts()
test_counts = y_test.value_counts()

# Create bar chart
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))

train_counts.plot(kind='bar', ax=ax1, color='skyblue')
ax1.set_title('Training Set Distribution')
ax1.set_xlabel('Class')
ax1.set_ylabel('Count')

test_counts.plot(kind='bar', ax=ax2, color='salmon')
ax2.set_title('Test Set Distribution')
ax2.set_xlabel('Class')
ax2.set_ylabel('Count')

plt.tight_layout()
plt.show()

# Translation: "Show side-by-side: how many 0s vs 1s in train and test"

#### When to Use Each Method

**Use pandas built-in (Method 1) when:**
- Counting occurrences (`value_counts()`)
- Showing groupby aggregations (mean, sum, etc.)
- Quick exploration
- Categories already in your data

**Use manual plt.bar (Method 2) when:**
- Custom category groupings (combining quality scores into tiers)
- Specific colors per bar
- Adding value labels
- More control over positioning

**Use horizontal bars (barh) when:**
- Category names are long
- Many categories (10+)
- Easier to read left-to-right

---

#### Bar Chart vs Other Charts

| Chart | Use When |
|-------|----------|
| **Bar** | Comparing discrete categories (counts, averages) |
| **Histogram** | Distribution of ONE continuous variable |
| **Boxplot** | Distribution comparison across categories |

**Rule of thumb:**
- "How many of each?" → Bar chart (counts)
- "What's the average for each?" → Bar chart (aggregated)
- "How is this variable distributed?" → Histogram
- "How does distribution differ across groups?" → Boxplot
```

---

### Saving Figures

```python
# Pattern: Save first, show second
plt.savefig('visuals/filename.png', dpi=300, bbox_inches='tight')
plt.show()

# Common parameters:
# dpi=300          : High quality (print-ready)
# bbox_inches='tight' : Remove extra whitespace
# transparent=True : Transparent background (optional)

```

---

## 📈 Statistical Concepts

### Descriptive Statistics

```python
df.describe()  # All numeric columns
df['column'].describe()  # Single column

# Returns: count, mean, std, min, 25%, 50% (median), 75%, max

# Always check:
# - Mean vs Median (50%) → If far apart, data is skewed
# - Min/Max vs 75%/25% → Spot outliers
# - Std (standard deviation) → Spread of data
```

---

### Hypothesis Testing (t-test)

```python
from scipy import stats

# Step 1: Create two groups
group1 = df[df['category'] == 'A']['numeric_column']
group2 = df[df['category'] == 'B']['numeric_column']

# Step 2: Check what you're comparing (always do this first)
print(f"Group 1: n={len(group1)}, mean={group1.mean():.2f}")
print(f"Group 2: n={len(group2)}, mean={group2.mean():.2f}")

# Step 3: Run t-test
statistic, p_value = stats.ttest_ind(group1, group2, nan_policy='omit')

# Step 4: Interpret
print(f"T-statistic: {statistic:.4f}")
print(f"P-value: {p_value:.4f}")

if p_value < 0.05:
    print("Statistically significant difference (p < 0.05)")
else:
    print("Not statistically significant (p >= 0.05)")

# Translation:
# p < 0.05 = "Less than 5% chance this difference is random luck"
# p >= 0.05 = "Could be random chance, not convincing"

```

### Hypothesis Interpretation Guide

```python
# P-VALUE BUSINESS TRANSLATION
p < 0.05:  "This difference is real, not random chance (95% confident)"
p >= 0.05: "Could be random variation, need more evidence"

# PRACTICAL SIGNIFICANCE CHECK
if p_value < 0.05:
    diff = group1.mean() - group2.mean()
    if abs(diff) > threshold:  # e.g., $50 for price
        print("Statistically AND practically significant")
    else:
        print("Statistically significant but too small to matter")
```

### Correlation

```python
# Calculate correlation coefficient
correlation = df['column1'].corr(df['column2'])
print(f"Correlation: {correlation:.2f}")

# Interpretation:
# +1.0 = Perfect positive (as X increases, Y increases)
# -1.0 = Perfect negative (as X increases, Y decreases)
#  0.0 = No linear relationship
# ±0.7-1.0 = Strong
# ±0.4-0.7 = Moderate
# ±0.0-0.4 = Weak

# REMEMBER: Correlation ≠ Causation

```

---

## 🗄️ SQL Basics

### Query Execution Order

```sql
-- Written order:
SELECT columns
FROM table
WHERE condition
GROUP BY category
HAVING aggregate_condition
ORDER BY column

-- Execution order:
1. FROM - Get the table
2. WHERE - Filter individual ROWS (before grouping)
3. GROUP BY - Pile rows into groups
4. HAVING - Filter GROUPS (after grouping)
5. SELECT - Choose columns to show
6. ORDER BY - Sort final output

-- Key insight:
-- WHERE filters ROWS (before grouping)
-- HAVING filters GROUPS (after grouping)
-- Can't use aggregate functions in WHERE clause

```

---

### Common Patterns

```sql
-- Basic aggregation
SELECT city, AVG(price) as avg_price, COUNT(*) as listing_count
FROM listings
GROUP BY city
ORDER BY avg_price DESC;

-- Filter groups with HAVING
SELECT neighborhood, AVG(price) as avg_price
FROM listings
GROUP BY neighborhood
HAVING COUNT(*) >= 10  -- Only neighborhoods with 10+ listings
ORDER BY avg_price DESC;

-- WHERE + GROUP BY + HAVING
SELECT property_type, AVG(price) as avg_price
FROM listings
WHERE price < 1000  -- Filter rows first
GROUP BY property_type
HAVING COUNT(*) >= 5  -- Then filter groups
ORDER BY avg_price DESC;

```

---

### CASE WHEN (Creating Categories)

```sql
-- Basic pattern
CASE
    WHEN condition1 THEN 'Label A'
    WHEN condition2 THEN 'Label B'
    ELSE 'Label C'
END as new_column_name

-- Real example
SELECT
    neighborhood,
    price,
    CASE
        WHEN review_scores_rating >= 4.9 THEN 'Excellent'
        WHEN review_scores_rating >= 4.5 THEN 'Good'
        ELSE 'Average'
    END as rating_category
FROM listings;

```

---

### Using SQL with Pandas

```python
import pandas as pd
import sqlite3

# Load CSV into SQLite database
df = pd.read_csv('data/raw/file.csv')
conn = sqlite3.connect('database.db')
df.to_sql('table_name', conn, if_exists='replace', index=False)

# Write SQL query
query = """
SELECT neighborhood, COUNT(*) as count, AVG(price) as avg_price
FROM table_name
WHERE price < 1000
GROUP BY neighborhood
HAVING COUNT(*) >= 5
ORDER BY avg_price DESC
"""

# Get results as DataFrame
results = pd.read_sql_query(query, conn)
print(results.head(10))
conn.close()

# Translation: "SQL lives in database, pandas gets results"

```

---

## 🐍 Python Quick Hits

### New Lines in Print

```python
# Pattern 1: \n inside f-string
print(f"True Negatives: {tn}\nFalse Positives: {fp}")

# Pattern 2: Multiple variables with \n between
print(tn, "\n", fp)

# Pattern 3: Separate print statements (adds newline automatically)
print(f"True Negatives: {tn}")
print(f"False Positives: {fp}")

# Pattern 4: Triple-quoted string (multi-line)
print(f"""
True Negatives: {tn}
False Positives: {fp}
False Negatives: {fn}
True Positives: {tp}
""")

# Translation: "\n = newline character, works anywhere in strings"
```

---

### Strings

```python
# Split into words and count
len(string.split())  # Splits on spaces
len(string.split(','))  # Splits on commas

# Replace text
string.replace('old', 'new')  # Replaces ALL occurrences
string.replace('old', 'new', 1)  # Replace only first

# Example
sentence = "I love coffee and coffee is great"
sentence.replace('coffee', 'Python')
# Returns: "I love Python and Python is great"

```

---

### Dictionaries

```python
# Create dictionary from two lists
keys = ['a', 'b', 'c']
values = [1, 2, 3]
my_dict = dict(zip(keys, values))
# Returns: {'a': 1, 'b': 2, 'c': 3}

# Add or update item
my_dict['d'] = 4  # Adds new key-value pair
my_dict['a'] = 10  # Updates existing value

# Calculate average of values
average = sum(my_dict.values()) / len(my_dict.values())

# Filter items above average
for key, value in my_dict.items():
    if value > average:
        print(f"{key}: {value}")

# Combining keys:values from a dictionary
# Sample dictionary
d = {'prices': [200, 350, 400], 'sqft': [1200, 1800, 2100]}

# Option 1: Zip into paired tuples
combined = list(zip(d['prices'], d['sqft']))
# Result: [(200, 1200), (350, 1800), (400, 2100)]
# Translation: "Pair up values by position"

# Option 2: Concatenate into one flat list
combined = d['prices'] + d['sqft']
# Result: [200, 350, 400, 1200, 1800, 2100]
# Translation: "Stick one list after the other"

# Option 3: Unpack multiple keys dynamically
keys_to_combine = ['prices', 'sqft']
combined = list(zip(*[d[k] for k in keys_to_combine]))
# Result: [(200, 1200), (350, 1800), (400, 2100)]
# Translation: "Zip values from any keys I specify"
```

---

### List Comprehension

```python
# Basic pattern (conditional EXPRESSION - transforms ALL items)
[value_if_true if condition else value_if_false for item in iterable]

# Your task - correct syntax
new_list = [f"High,{num}" if num > 20 else f"Low,{num}" for num in first_list]
# Translation: "For each number, return 'High,{num}' if >20, otherwise 'Low,{num}'"

# Simpler version (just "High" or "Low" without number)
new_list = ["High" if num > 20 else "Low" for num in first_list]

# Filter (if at the end)
[item for item in list if condition]
# "Give me items WHERE condition is true"
# Result: FEWER items (some excluded)

# Transform (if/else at the beginning)
[value_if_true if condition else value_if_false for item in list]
# "Give me ALL items, but CHANGE them based on condition"
# Result: SAME number of items (all transformed)
```

---

### Random

```python
# Your version (works perfectly)
first_list = list(random.sample(range(1, 30), k=15))

# Cleaner (random.sample() already returns a list)
first_list = random.sample(range(1, 30), k=15)

# ✅ Your approach: random.sample() - NO DUPLICATES
first_list = random.sample(range(1, 30), k=15)
# Translation: "Give me 15 unique random numbers from 1-29"
# Result: [3, 27, 8, 15, ...] all different

# Alternative: random.choices() - DUPLICATES ALLOWED
first_list = random.choices(range(1, 30), k=15)
# Translation: "Give me 15 random numbers (can repeat)"
# Result: [3, 27, 3, 15, 3, ...] might have repeats

# Alternative: List comprehension with randint
first_list = [random.randint(1, 30) for _ in range(15)]
# Same as choices (duplicates allowed)
```

---

### Shell Commands in Jupyter

```python
# List files
!ls  # Current directory
!ls data/raw/  # Specific directory
!pwd  # Current working directory

# Find files
!find . -name "*.csv"  # Find CSV files
!find ~/repos -name "*airbnb*"  # Find files with 'airbnb' in name

# Alternative: Python's glob module
import glob
csv_files = glob.glob('data/raw/*.csv')
print(csv_files)

# Find all CSVs recursively
all_csvs = glob.glob('**/*.csv', recursive=True)

```

---

## Git Quick Reference

### Daily Workflow

```bash
git status                      # What's changed?
git add .                       # Stage all changes
git commit -m "message"         # Commit with message
git push                        # Push to remote
git pull                        # Get latest from remote
git log --oneline -10           # Last 10 commits (compact)

```

### Branching (Module 4+)

```bash
git branch                      # List branches
git checkout -b feature-name    # Create and switch to new branch
git checkout main               # Switch to main
git merge feature-name          # Merge branch into current
git branch -d feature-name      # Delete branch (after merge)

```

### Undoing Things

```bash
git restore filename.py         # Discard unstaged changes to file
git restore --staged filename   # Unstage file (keep changes)
git stash                       # Temporarily save uncommitted work
git stash pop                   # Restore stashed work
git commit --amend -m "new msg" # Fix last commit message

```

### Checking History

```bash
git diff                        # See unstaged changes
git diff --staged               # See staged changes
git log --oneline --graph       # Visual branch history

```

---

## Bash Quick Reference

### Navigation

```bash
cd path/to/folder               # Change directory
cd ..                           # Go up one level
cd ~                            # Go to home directory
cd -                            # Go to previous directory
pwd                             # Print current directory
ls                              # List files
ls -la                          # List all with details

```

### File Operations

```bash
touch filename.py               # Create empty file
mkdir foldername                # Create directory
mkdir -p path/to/nested         # Create nested directories
cp source dest                  # Copy file
cp -r source dest               # Copy directory
mv source dest                  # Move or rename
rm filename                     # Remove file
rm -r foldername                # Remove directory
rm -rf foldername               # Force remove (DANGEROUS)

```

### Viewing Files

```bash
cat filename                    # Print entire file
head -n 20 filename             # First 20 lines
tail -n 20 filename             # Last 20 lines
less filename                   # Scrollable viewer (q to quit)
wc -l filename                  # Count lines

```

### Piping & Redirection

```bash
echo "text" > file.txt          # Write to file (overwrite)
echo "text" >> file.txt         # Append to file
cmd1 | cmd2                     # Pipe output to next command
cat file.txt | grep "pattern"   # Find lines with pattern

```

### Search

```bash
grep "pattern" filename         # Find pattern in file
grep -r "pattern" ./folder      # Recursive search in folder
grep -i "pattern" filename      # Case-insensitive
grep -n "pattern" filename      # Show line numbers
find . -name "*.py"             # Find all Python files

```

### Environment

```bash
echo $PATH                      # Print PATH variable
export VAR="value"              # Set environment variable
which python                    # Find command location

```

### Process Management

```bash
Ctrl+C                          # Stop current command
Ctrl+Z                          # Suspend current command
ps aux | grep python            # Find Python processes
kill 12345                      # Terminate process by PID

```

### Permissions

```bash
chmod +x script.sh              # Make file executable
sudo command                    # Run as superuser

```

---

## Markdown Quick Reference

### Headers

```markdown
# H1 - Main Title
## H2 - Section
### H3 - Subsection
#### H4 - Sub-subsection

```

### Text Formatting

```markdown
**bold text**
*italic text*
***bold and italic***
~~strikethrough~~
`inline code`

```

### Lists

```markdown
- Bullet point
- Another bullet
  - Nested bullet (2 spaces)

1. Numbered item
2. Second item
   1. Nested number (3 spaces)

```

### Links & Images

```markdown
Link Text
Link with Title

!Alt text
!Alt text

```

### Code Blocks

```markdown
Inline: `code here`

Block (use triple backticks):
```python
def hello():
    print("Hello")
```

```

### Blockquotes

```markdown
> This is a quote
> Continues on next line
>
> New paragraph in quote

```

### Horizontal Rule

```markdown
---

```

### Tables

```markdown
| Column 1 | Column 2 | Column 3 |
|----------|----------|----------|
| Row 1    | Data     | Data     |
| Row 2    | Data     | Data     |

| Left | Center | Right |
|:-----|:------:|------:|
| L    |   C    |     R |

```

### Task Lists

```markdown
- [ ] Unchecked task
- [x] Completed task
- [ ] Another task

```

### Escaping Characters

```markdown
\\* literal asterisk
\\# literal hash
\\` literal backtick
\\| literal pipe

```

### Common Gotchas

```markdown
# Blank line required before:
- Lists
- Code blocks
- Tables

# Two spaces at end of line = line break
This line ends with two spaces
This is on a new line

# Or use <br> for explicit break
Line one<br>Line two

```