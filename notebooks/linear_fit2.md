Since I don't have access to your specific local file, I have written this script to be 
**modular**. I have also included a block at the beginning that **generates a dummy CSV file** so 
you can run the script immediately to see how it works.

You can replace `'your_data.csv'` with the actual path to your file.

```python
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import os

# ==========================================
# STEP 0: Create a dummy file (For demonstration)
# This part ensures the script runs even if you don't have a file ready.
# ==========================================
def create_dummy_data(filename):
    data = {
        'sqft': [1500, 1800, 2400, 3000, 3500, 4000, 1200, 2200, 2800, 3200],
        'bedrooms': [3, 3, 4, 4, 5, 5, 2, 3, 4, 4],
        'age': [10, 15, 5, 2, 1, 20, 30, 12, 8, 5],
        'price': [300000, 350000, 450000, 550000, 600000, 650000, 200000, 400000, 500000, 580000]
    }
    df = pd.DataFrame(data)
    # Adding some NaN values to demonstrate the "formatting/cleaning" step
    df.loc[2, 'age'] = np.nan 
    df.to_csv(filename, index=False)
    print(f"--- Dummy file '{filename}' created ---\n")

# ==========================================
# STEP 1: Main Processing Pipeline
# ==========================================
def run_linear_regression_pipeline(file_path, target_column):
    try:
        # 1. Load the local data file
        print(f"Loading data from: {file_path}")
        df = pd.read_csv(file_path)
        
        # 2. Formatting and Cleaning
        print("Cleaning and formatting data...")
        
        # Drop duplicate rows
        df = df.drop_duplicates()
        
        # Handle Missing Values: 
        # In this example, we fill numeric NaNs with the median of that column
        numeric_cols = df.select_dtypes(include=[np.number]).columns
        df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].median())
        
        # Ensure all features are numeric (in case strings were present)
        df[numeric_cols] = df[numeric_cols].apply(pd.to_numeric, errors='coerce')
        
        # Drop any rows that became NaN after coercion
        df = df.dropna()

        print("Cleaned Data Preview:")
        print(df.head(), "\n")

        # 3. Prepare Data for Modeling
        # X = Features (all columns except the target)
        # y = Target (the column we want to predict)
        X = df.drop(columns=[target_column])
        y = df[target_column]

        # Split into Training and Testing sets (80% train, 20% test)
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # 4. Initialize and Train the Model
        print(f"Training Linear Regression model to predict '{target_column}'...")
        model = LinearRegression()
        model.fit(X_train, y_train)

        # 5. Make Predictions and Evaluate
        predictions = model.predict(X_test)
        
        mse = mean_squared_error(y_test, predictions)
        r2 = r2_score(y_test, predictions)

        print("--- Model Results ---")
        print(f"Mean Squared Error: {mse:.2f}")
        print(f"R-squared Score:    {r2:.2f}")
        print("\nCoefficients:", dict(zip(X.columns, model.coef_)))
        print(f"Intercept: {model.intercept_:.2f}")

    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except KeyError:
        print(f"Error: The column '{target_column}' does not exist in the dataset.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# ==========================================
# EXECUTION
# ==========================================
if __name__ == "__main__":
    DATA_FILENAME = 'my_local_data.csv'
    TARGET_COL = 'price' # Change this to your actual target column name

    # Create dummy data so the script works immediately
    create_dummy_data(DATA_FILENAME)

    # Run the pipeline
    run_linear_regression_pipeline(DATA_FILENAME, TARGET_COL)
```

### Key Features of this Script:

1.  **Robust Cleaning:**
    *   **`drop_duplicates()`**: Removes redundant data.
    *   **`fillna(df.median())`**: Automatically identifies numeric columns and fills missing 
values with the median (this prevents the model from crashing due to `NaN` values).
    *   **`pd.to_numeric`**: Ensures that data intended to be numbers isn't being treated as 
"object" (string) types, which is a common cause of errors in `scikit-learn`.
2.  **Automated Feature Splitting:** It automatically treats every column in your file as a feature 
($X$), provided you tell it which single column is the target ($y$).
3.  **Error Handling:** I wrapped the logic in a `try-except` block. If your file is missing or you 
misspell the target column name, it will give you a readable error instead of a messy traceback.
4.  **Evaluation Metrics:** It provides both **MSE** (how far off the predictions are) and 
**$R^2$** (how well the model fits the data).

### How to use it with your own data:
1.  Change `DATA_FILENAME = 'my_local_data.csv'` to your actual filename (e.g., 
`'sales_data.csv'`).
2.  Change `TARGET_COL = 'price'` to the name of the column you want to 
predict.
3.  Ensure your CSV file has no text-based categories in the feature columns (if you have 
text categories like "City" or "Color", you would need to add a "One-Hot Encoding" step, which is 
the next level of complexity).