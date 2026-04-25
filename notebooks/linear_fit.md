```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import pandas as pd

def linear_regression_analysis(X, y, feature_names=None, target_name='Target', 
                            title="Linear Regression Analysis", 
                            figsize=(10, 6)):
    """
    Perform linear regression analysis on given data and display results.
    
    Parameters:
    X (array-like): Independent variables (features)
    y (array-like): Dependent variable (target)
    feature_names (list): Names of features (optional)
    target_name (str): Name of target variable
    title (str): Title for the plot
    figsize (tuple): Figure size for the plot
    
    Returns:
    dict: Dictionary containing model, r2_score, and other metrics
    """
    
    # Convert to numpy arrays if needed
    X = np.array(X)
    y = np.array(y)
    
    # Handle case where X is 1D
    if X.ndim == 1:
        X = X.reshape(-1, 1)
    
    # Create and fit the model
    model = LinearRegression()
    model.fit(X, y)
    
    # Make predictions
    y_pred = model.predict(X)
    
    # Calculate R2 score
    r2 = r2_score(y, y_pred)
    
    # Calculate additional metrics
    n = len(y)
    p = X.shape[1]  # number of features
    adj_r2 = 1 - (1 - r2) * (n - 1) / (n - p - 1)
    
    # Create the plot
    plt.figure(figsize=figsize)
    
    # Plot scatter points for each feature
    if X.shape[1] == 1:
        # Single feature case
        plt.scatter(X, y, c='blue', alpha=0.7, s=50, label='Data points')
        plt.scatter(X, y_pred, c='red', alpha=0.7, s=50, marker='x', label='Predicted')
    else:
        # Multiple features case - plot each feature separately
        colors = plt.cm.Set3(np.linspace(0, 1, X.shape[1]))
        for i in range(X.shape[1]):
            plt.scatter(X[:, i], y, c=[colors[i]], alpha=0.7, s=50, 
                       label=f'{feature_names[i] if feature_names else f"Feature {i+1}"}')
    
    # Plot the regression line (for single feature case)
    if X.shape[1] == 1:
        # Create a smooth line for the regression
        X_line = np.linspace(X.min(), X.max(), 100).reshape(-1, 1)
        y_line = model.predict(X_line)
        plt.plot(X_line, y_line, 'r-', linewidth=2, label='Regression line')
    
    # Add labels and title
    if X.shape[1] == 1:
        plt.xlabel(feature_names[0] if feature_names else 'X')
    else:
        plt.xlabel('Features')
    plt.ylabel(target_name)
    plt.title(title)
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    # Add R2 score to the plot
    plt.text(0.05, 0.95, f'R² = {r2:.4f}\nAdjusted R² = {adj_r2:.4f}', 
             transform=plt.gca().transAxes, verticalalignment='top',
             bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))
    
    plt.tight_layout()
    plt.show()
    
    # Print summary
    print(f"Linear Regression Summary")
    print("=" * 50)
    print(f"R² Score: {r2:.6f}")
    print(f"Adjusted R² Score: {adj_r2:.6f}")
    print(f"Number of observations: {n}")
    print(f"Number of features: {p}")
    print(f"Coefficients: {model.coef_}")
    print(f"Intercept: {model.intercept_:.6f}")
    
    if X.shape[1] == 1:
        print(f"Slope: {model.coef_[0]:.6f}")
        print(f"Equation: y = {model.coef_[0]:.6f}x + {model.intercept_:.6f}")
    
    # Return model and metrics
    results = {
        'model': model,
        'r2_score': r2,
        'adjusted_r2': adj_r2,
        'coefficients': model.coef_,
        'intercept': model.intercept_,
        'predictions': y_pred,
        'residuals': y - y_pred
    }
    
    return results

# Example usage:
if __name__ == "__main__":
    # Generate sample data
    np.random.seed(42)
    n_samples = 100
    
    # Create multiple features
    X1 = np.random.randn(n_samples)
    X2 = np.random.randn(n_samples)
    X3 = np.random.randn(n_samples)
    
    # Create target variable with some relationship to features
    y = 2*X1 + 1.5*X2 - 0.5*X3 + np.random.randn(n_samples)*0.5
    
    # Example 1: Single feature
    print("Example 1: Single Feature Analysis")
    results1 = linear_regression_analysis(X1, y, 
                                        feature_names=['Feature 1'], 
                                        target_name='Target Variable')
    
    print("\n" + "="*50 + "\n")
    
    # Example 2: Multiple features
    print("Example 2: Multiple Features Analysis")
    X_multi = np.column_stack([X1, X2, X3])
    results2 = linear_regression_analysis(X_multi, y, 
                                        feature_names=['Feature 1', 'Feature 2', 'Feature 3'], 
                                        target_name='Target Variable')
```

This function provides a comprehensive linear regression analysis with the following features:

## Key Features:

1. **Model Training**: Uses scikit-learn's LinearRegression to fit the model
2. **R² Score Calculation**: Computes both regular and adjusted R² scores
3. **Visual Display**: 
   - Scatter plot with different colors for each variable
   - Solid red line showing the linear correlation
   - Data points with prediction markers
4. **Comprehensive Summary**: Prints detailed statistics including coefficients, intercept, and R² values

## Function Parameters:

- `X`: Independent variables (features)
- `y`: Dependent variable (target)
- `feature_names`: Optional list of feature names
- `target_name`: Name of the target variable
- `title`: Plot title
- `figsize`: Figure size for visualization

## Output:

- **Plot**: Scatter plot with regression line and different colored points
- **Console Output**: Detailed summary including R² scores, coefficients, and model parameters
- **Return Value**: Dictionary containing model object and all calculated metrics

## Usage Examples:

The code includes two examples:
1. Single feature linear regression
2. Multiple feature linear regression with three different colored variables

The function handles both single and multiple feature cases appropriately, making it flexible for various datasets.
