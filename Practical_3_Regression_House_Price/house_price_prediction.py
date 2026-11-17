"""
Practical Assignment No. 3: House Price Prediction Using Regression Models
Author: Shruti Siddheshwar Thorat
PRN: 202401040053 | Roll No: 16 | Batch: A1
Aim: Implement and compare Simple Linear Regression, Multiple Linear Regression,
     and Polynomial Regression using both library-based and manual approaches.
"""

import os



import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import (
    mean_squared_error,
    mean_absolute_error,
    r2_score
)

# Load dataset directly from GitHub
url = "https://raw.githubusercontent.com/Komalharini237/Housing-Case-Study-Multiple-Linear-Regression/main/Housing.csv"

if os.path.exists("Housing.csv"):
    df = pd.read_csv("Housing.csv")
else:
    df = pd.read_csv(url)

# Display the first five records
print("FIRST FIVE RECORDS")
print(df.head())

print("Dataset shape:", df.shape)
print("Column names:", df.columns.tolist())



print("DATASET INFORMATION")
print("--------------------")
print("Number of rows:", df.shape[0])
print("Number of columns:", df.shape[1])

print("\nColumn data types:")
print(df.dtypes)

print("\nStatistical summary:")
print(df.describe())

print("\nMissing values:")
print(df.isnull().sum())

print("\nDuplicate rows:", df.duplicated().sum())



# Remove duplicate records
df = df.drop_duplicates().copy()

# Select numerical input features
features = [
    "area",
    "bedrooms",
    "bathrooms",
    "stories",
    "parking"
]

target = "price"

# Convert selected columns to numeric values
for col in features + [target]:
    df[col] = pd.to_numeric(df[col], errors="coerce")

# Replace infinite values and handle missing values
df = df.replace([np.inf, -np.inf], np.nan)

df[features] = df[features].fillna(df[features].median())
df[target] = df[target].fillna(df[target].median())

# Keep only valid, positive house prices and areas
df = df[(df["price"] > 0) & (df["area"] > 0)].copy()

X = df[features]
y = df[target]

print("Preprocessing completed.")
print("Records after cleaning:", len(df))
print("Selected input features:", features)
print("Target variable:", target)
print("Remaining missing values:", df[features + [target]].isnull().sum().sum())



# Graph 1: Distribution of house prices
plt.figure(figsize=(8, 5))
plt.hist(df["price"], bins=20, edgecolor="black")
plt.title("Distribution of House Prices")
plt.xlabel("House Price")
plt.ylabel("Number of Houses")
plt.tight_layout()
plt.show()

# Graph 2: Area versus price
plt.figure(figsize=(8, 5))
plt.scatter(df["area"], df["price"], alpha=0.65)
plt.title("House Area vs House Price")
plt.xlabel("Area")
plt.ylabel("House Price")
plt.tight_layout()
plt.show()

# Graph 3: Number of bedrooms versus price
bedroom_prices = df.groupby("bedrooms")["price"].mean()

plt.figure(figsize=(8, 5))
plt.bar(bedroom_prices.index.astype(str), bedroom_prices.values)
plt.title("Average House Price by Number of Bedrooms")
plt.xlabel("Number of Bedrooms")
plt.ylabel("Average House Price")
plt.tight_layout()
plt.show()

# Graph 4: Correlation heatmap for numerical variables
corr = df[features + [target]].corr()

plt.figure(figsize=(8, 6))
plt.imshow(corr, cmap="coolwarm", vmin=-1, vmax=1)
plt.colorbar(label="Correlation")
plt.xticks(range(len(corr.columns)), corr.columns, rotation=45, ha="right")
plt.yticks(range(len(corr.columns)), corr.columns)

for i in range(len(corr.columns)):
    for j in range(len(corr.columns)):
        plt.text(j, i, f"{corr.iloc[i, j]:.2f}",
                 ha="center", va="center", fontsize=9)

plt.title("Correlation Heatmap")
plt.tight_layout()
plt.show()



# Split the complete numerical feature set
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)

# Split the single-feature dataset for simple regression
X_simple_train = X_train[["area"]]
X_simple_test = X_test[["area"]]

print("Training records:", len(X_train))
print("Testing records:", len(X_test))



# Train the model
simple_model = LinearRegression()
simple_model.fit(X_simple_train, y_train)

# Predict test values
simple_pred_lib = simple_model.predict(X_simple_test)

# Calculate evaluation metrics
simple_mse_lib = mean_squared_error(y_test, simple_pred_lib)
simple_rmse_lib = np.sqrt(simple_mse_lib)
simple_mae_lib = mean_absolute_error(y_test, simple_pred_lib)
simple_r2_lib = r2_score(y_test, simple_pred_lib)

print("SIMPLE LINEAR REGRESSION WITH LIBRARY")
print("------------------------------------")
print("Intercept:", simple_model.intercept_)
print("Slope:", simple_model.coef_[0])
print("MSE:", simple_mse_lib)
print("RMSE:", simple_rmse_lib)
print("MAE:", simple_mae_lib)
print("R2 Score:", simple_r2_lib)

# Graph 1: Actual versus predicted prices
plt.figure(figsize=(8, 5))
plt.scatter(y_test, simple_pred_lib, alpha=0.7)

low = min(y_test.min(), simple_pred_lib.min())
high = max(y_test.max(), simple_pred_lib.max())
plt.plot([low, high], [low, high], "r--", label="Perfect prediction")

plt.xlabel("Actual House Price")
plt.ylabel("Predicted House Price")
plt.title("Simple Linear Regression: Actual vs Predicted")
plt.legend()
plt.tight_layout()
plt.show()

# Graph 2: Regression line
plt.figure(figsize=(8, 5))
plt.scatter(X_simple_train["area"], y_train,
            alpha=0.6, label="Training data")

area_line = np.linspace(
    X_simple_train["area"].min(),
    X_simple_train["area"].max(),
    200
)

price_line = simple_model.predict(
    pd.DataFrame({"area": area_line})
)

plt.plot(area_line, price_line, "r-", linewidth=2,
         label="Regression line")

plt.xlabel("House Area")
plt.ylabel("House Price")
plt.title("Simple Linear Regression: Regression Line")
plt.legend()
plt.tight_layout()
plt.show()



# Convert training data to NumPy arrays
x_train = X_simple_train["area"].to_numpy(dtype=float)
x_test = X_simple_test["area"].to_numpy(dtype=float)

y_train_arr = y_train.to_numpy(dtype=float)
y_test_arr = y_test.to_numpy(dtype=float)

# Calculate slope and intercept manually
x_mean = np.mean(x_train)
y_mean = np.mean(y_train_arr)

slope_manual = np.sum(
    (x_train - x_mean) * (y_train_arr - y_mean)
) / np.sum((x_train - x_mean) ** 2)

intercept_manual = y_mean - slope_manual * x_mean

# Predict test values
simple_pred_manual = intercept_manual + slope_manual * x_test

# Evaluation metrics
simple_mse_manual = mean_squared_error(
    y_test_arr, simple_pred_manual
)
simple_rmse_manual = np.sqrt(simple_mse_manual)
simple_mae_manual = mean_absolute_error(
    y_test_arr, simple_pred_manual
)
simple_r2_manual = r2_score(y_test_arr, simple_pred_manual)

print("SIMPLE LINEAR REGRESSION WITHOUT LIBRARY")
print("---------------------------------------")
print("Intercept:", intercept_manual)
print("Slope:", slope_manual)
print("MSE:", simple_mse_manual)
print("RMSE:", simple_rmse_manual)
print("MAE:", simple_mae_manual)
print("R2 Score:", simple_r2_manual)

# Actual versus predicted graph
plt.figure(figsize=(8, 5))
plt.scatter(y_test_arr, simple_pred_manual, alpha=0.7)

low = min(y_test_arr.min(), simple_pred_manual.min())
high = max(y_test_arr.max(), simple_pred_manual.max())
plt.plot([low, high], [low, high], "r--",
         label="Perfect prediction")

plt.xlabel("Actual House Price")
plt.ylabel("Predicted House Price")
plt.title("Simple Linear Regression Without Library")
plt.legend()
plt.tight_layout()
plt.show()



simple_comparison = pd.DataFrame({
    "Metric": ["MSE", "RMSE", "MAE", "R2 Score"],
    "With Library": [
        simple_mse_lib, simple_rmse_lib,
        simple_mae_lib, simple_r2_lib
    ],
    "Without Library": [
        simple_mse_manual, simple_rmse_manual,
        simple_mae_manual, simple_r2_manual
    ]
})

print(simple_comparison.round(4))

# Compare error metrics
simple_comparison.set_index("Metric").loc[
    ["MSE", "RMSE", "MAE"]
].plot(kind="bar", figsize=(8, 5))

plt.title("Simple Linear Regression: Error Comparison")
plt.ylabel("Metric Value")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

# Compare R2 separately
simple_comparison.set_index("Metric").loc[
    ["R2 Score"]
].plot(kind="bar", figsize=(6, 4))

plt.title("Simple Linear Regression: R2 Comparison")
plt.ylabel("R2 Score")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()



# Train multiple linear regression
multiple_model = LinearRegression()
multiple_model.fit(X_train, y_train)

# Predict test prices
multiple_pred_lib = multiple_model.predict(X_test)

# Evaluate
multiple_mse_lib = mean_squared_error(y_test, multiple_pred_lib)
multiple_rmse_lib = np.sqrt(multiple_mse_lib)
multiple_mae_lib = mean_absolute_error(y_test, multiple_pred_lib)
multiple_r2_lib = r2_score(y_test, multiple_pred_lib)

print("MULTIPLE LINEAR REGRESSION WITH LIBRARY")
print("--------------------------------------")
print("Intercept:", multiple_model.intercept_)

print("\nFeature coefficients:")
for name, coef in zip(features, multiple_model.coef_):
    print(f"{name}: {coef:.4f}")

print("\nMSE:", multiple_mse_lib)
print("RMSE:", multiple_rmse_lib)
print("MAE:", multiple_mae_lib)
print("R2 Score:", multiple_r2_lib)

# Actual versus predicted graph
plt.figure(figsize=(8, 5))
plt.scatter(y_test, multiple_pred_lib, alpha=0.7)

low = min(y_test.min(), multiple_pred_lib.min())
high = max(y_test.max(), multiple_pred_lib.max())
plt.plot([low, high], [low, high], "r--",
         label="Perfect prediction")

plt.xlabel("Actual House Price")
plt.ylabel("Predicted House Price")
plt.title("Multiple Linear Regression: Actual vs Predicted")
plt.legend()
plt.tight_layout()
plt.show()



# Convert features and targets to NumPy arrays
X_train_arr = X_train.to_numpy(dtype=float)
X_test_arr = X_test.to_numpy(dtype=float)

y_train_arr = y_train.to_numpy(dtype=float)
y_test_arr = y_test.to_numpy(dtype=float)

# Standardize using training data only
X_mean = X_train_arr.mean(axis=0)
X_std = X_train_arr.std(axis=0)
X_std[X_std == 0] = 1

X_train_scaled = (X_train_arr - X_mean) / X_std
X_test_scaled = (X_test_arr - X_mean) / X_std

y_mean = y_train_arr.mean()
y_std = y_train_arr.std()

y_train_scaled = (y_train_arr - y_mean) / y_std

# Add a column of ones for the intercept
X_train_b = np.column_stack([
    np.ones(len(X_train_scaled)), X_train_scaled
])
X_test_b = np.column_stack([
    np.ones(len(X_test_scaled)), X_test_scaled
])

# Initialize coefficients
weights = np.zeros(X_train_b.shape[1])

learning_rate = 0.03
epochs = 10000
n = len(y_train_scaled)

cost_history = []

# Gradient descent
for epoch in range(epochs):
    predictions = X_train_b @ weights
    errors = predictions - y_train_scaled

    gradients = (2 / n) * (X_train_b.T @ errors)
    weights -= learning_rate * gradients

    cost = np.mean((X_train_b @ weights - y_train_scaled) ** 2)
    cost_history.append(cost)

# Predict and convert to original price units
multiple_pred_manual = (
    X_test_b @ weights
) * y_std + y_mean

# Evaluation
multiple_mse_manual = mean_squared_error(
    y_test_arr, multiple_pred_manual
)
multiple_rmse_manual = np.sqrt(multiple_mse_manual)
multiple_mae_manual = mean_absolute_error(
    y_test_arr, multiple_pred_manual
)
multiple_r2_manual = r2_score(
    y_test_arr, multiple_pred_manual
)

print("MULTIPLE LINEAR REGRESSION WITHOUT LIBRARY")
print("-----------------------------------------")
print("Intercept in standardized model:", weights[0])
print("MSE:", multiple_mse_manual)
print("RMSE:", multiple_rmse_manual)
print("MAE:", multiple_mae_manual)
print("R2 Score:", multiple_r2_manual)

# Actual versus predicted graph
plt.figure(figsize=(8, 5))
plt.scatter(y_test_arr, multiple_pred_manual, alpha=0.7)

low = min(y_test_arr.min(), multiple_pred_manual.min())
high = max(y_test_arr.max(), multiple_pred_manual.max())
plt.plot([low, high], [low, high], "r--",
         label="Perfect prediction")

plt.xlabel("Actual House Price")
plt.ylabel("Predicted House Price")
plt.title("Multiple Linear Regression Without Library")
plt.legend()
plt.tight_layout()
plt.show()

# Gradient descent convergence graph
plt.figure(figsize=(8, 5))
plt.plot(cost_history)
plt.xlabel("Epoch")
plt.ylabel("Mean Squared Error on Scaled Target")
plt.title("Gradient Descent Convergence")
plt.tight_layout()
plt.show()



multiple_comparison = pd.DataFrame({
    "Metric": ["MSE", "RMSE", "MAE", "R2 Score"],
    "With Library": [
        multiple_mse_lib, multiple_rmse_lib,
        multiple_mae_lib, multiple_r2_lib
    ],
    "Without Library": [
        multiple_mse_manual, multiple_rmse_manual,
        multiple_mae_manual, multiple_r2_manual
    ]
})

print(multiple_comparison.round(4))

# Error metrics comparison
multiple_comparison.set_index("Metric").loc[
    ["MSE", "RMSE", "MAE"]
].plot(kind="bar", figsize=(8, 5))

plt.title("Multiple Regression: Error Metrics Comparison")
plt.ylabel("Metric Value")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

# R2 comparison
multiple_comparison.set_index("Metric").loc[
    ["R2 Score"]
].plot(kind="bar", figsize=(6, 4))

plt.title("Multiple Regression: R2 Score Comparison")
plt.ylabel("R2 Score")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()



# Use house area as the single input feature
poly_mean = X_simple_train["area"].mean()
poly_std = X_simple_train["area"].std()

if poly_std == 0:
    poly_std = 1

z_train = (
    X_simple_train["area"].to_numpy(dtype=float) - poly_mean
) / poly_std

z_test = (
    X_simple_test["area"].to_numpy(dtype=float) - poly_mean
) / poly_std

# Create degree-2 polynomial features
poly_transformer = PolynomialFeatures(degree=2, include_bias=False)

Z_train_poly = poly_transformer.fit_transform(z_train.reshape(-1, 1))
Z_test_poly = poly_transformer.transform(z_test.reshape(-1, 1))

# Train polynomial regression
poly_model = LinearRegression()
poly_model.fit(Z_train_poly, y_train)

# Predict test prices
poly_pred_lib = poly_model.predict(Z_test_poly)

# Evaluation
poly_mse_lib = mean_squared_error(y_test, poly_pred_lib)
poly_rmse_lib = np.sqrt(poly_mse_lib)
poly_mae_lib = mean_absolute_error(y_test, poly_pred_lib)
poly_r2_lib = r2_score(y_test, poly_pred_lib)

print("POLYNOMIAL REGRESSION WITH LIBRARY")
print("---------------------------------")
print("Intercept:", poly_model.intercept_)
print("Coefficients:", poly_model.coef_)
print("MSE:", poly_mse_lib)
print("RMSE:", poly_rmse_lib)
print("MAE:", poly_mae_lib)
print("R2 Score:", poly_r2_lib)

# Actual versus predicted graph
plt.figure(figsize=(8, 5))
plt.scatter(y_test, poly_pred_lib, alpha=0.7)

low = min(y_test.min(), poly_pred_lib.min())
high = max(y_test.max(), poly_pred_lib.max())
plt.plot([low, high], [low, high], "r--",
         label="Perfect prediction")

plt.xlabel("Actual House Price")
plt.ylabel("Predicted House Price")
plt.title("Polynomial Regression: Actual vs Predicted")
plt.legend()
plt.tight_layout()
plt.show()

# Polynomial curve
z_line = np.linspace(z_train.min(), z_train.max(), 200)
z_line_poly = poly_transformer.transform(z_line.reshape(-1, 1))
price_line = poly_model.predict(z_line_poly)
area_line = z_line * poly_std + poly_mean

plt.figure(figsize=(8, 5))
plt.scatter(X_simple_train["area"], y_train,
            alpha=0.55, label="Training data")
plt.plot(area_line, price_line, "r-", linewidth=2,
         label="Polynomial curve")

plt.xlabel("House Area")
plt.ylabel("House Price")
plt.title("Polynomial Regression Curve")
plt.legend()
plt.tight_layout()
plt.show()



# Manually construct polynomial features
Z_train_manual = np.column_stack([
    np.ones(len(z_train)),
    z_train,
    z_train ** 2
])

Z_test_manual = np.column_stack([
    np.ones(len(z_test)),
    z_test,
    z_test ** 2
])

# Calculate coefficients using least squares
poly_coefficients, residuals, rank, singular_values = np.linalg.lstsq(
    Z_train_manual,
    y_train.to_numpy(dtype=float),
    rcond=None
)

# Predict test prices
poly_pred_manual = Z_test_manual @ poly_coefficients

# Evaluation
poly_mse_manual = mean_squared_error(
    y_test.to_numpy(dtype=float), poly_pred_manual
)
poly_rmse_manual = np.sqrt(poly_mse_manual)
poly_mae_manual = mean_absolute_error(
    y_test.to_numpy(dtype=float), poly_pred_manual
)
poly_r2_manual = r2_score(
    y_test.to_numpy(dtype=float), poly_pred_manual
)

print("POLYNOMIAL REGRESSION WITHOUT LIBRARY")
print("------------------------------------")
print("Intercept:", poly_coefficients[0])
print("Linear coefficient:", poly_coefficients[1])
print("Quadratic coefficient:", poly_coefficients[2])
print("MSE:", poly_mse_manual)
print("RMSE:", poly_rmse_manual)
print("MAE:", poly_mae_manual)
print("R2 Score:", poly_r2_manual)

# Actual versus predicted graph
plt.figure(figsize=(8, 5))
plt.scatter(y_test, poly_pred_manual, alpha=0.7)

low = min(y_test.min(), poly_pred_manual.min())
high = max(y_test.max(), poly_pred_manual.max())
plt.plot([low, high], [low, high], "r--",
         label="Perfect prediction")

plt.xlabel("Actual House Price")
plt.ylabel("Predicted House Price")
plt.title("Polynomial Regression Without Library")
plt.legend()
plt.tight_layout()
plt.show()

# Manual polynomial curve
price_line_manual = (
    poly_coefficients[0]
    + poly_coefficients[1] * z_line
    + poly_coefficients[2] * z_line ** 2
)

plt.figure(figsize=(8, 5))
plt.scatter(X_simple_train["area"], y_train,
            alpha=0.55, label="Training data")
plt.plot(area_line, price_line_manual, "r-",
         linewidth=2, label="Manual polynomial curve")

plt.xlabel("House Area")
plt.ylabel("House Price")
plt.title("Polynomial Regression Without Library")
plt.legend()
plt.tight_layout()
plt.show()



polynomial_comparison = pd.DataFrame({
    "Metric": ["MSE", "RMSE", "MAE", "R2 Score"],
    "With Library": [
        poly_mse_lib, poly_rmse_lib, poly_mae_lib, poly_r2_lib
    ],
    "Without Library": [
        poly_mse_manual, poly_rmse_manual,
        poly_mae_manual, poly_r2_manual
    ]
})

print(polynomial_comparison.round(4))

# Compare error metrics
polynomial_comparison.set_index("Metric").loc[
    ["MSE", "RMSE", "MAE"]
].plot(kind="bar", figsize=(8, 5))

plt.title("Polynomial Regression: Error Metrics Comparison")
plt.ylabel("Metric Value")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

# Compare R2 score separately
polynomial_comparison.set_index("Metric").loc[
    ["R2 Score"]
].plot(kind="bar", figsize=(6, 4))

plt.title("Polynomial Regression: R2 Score Comparison")
plt.ylabel("R2 Score")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()



# Combine all model results
final_results = pd.DataFrame([
    {
        "Model": "Simple Linear Regression",
        "Implementation": "With Library",
        "MSE": simple_mse_lib,
        "RMSE": simple_rmse_lib,
        "MAE": simple_mae_lib,
        "R2 Score": simple_r2_lib
    },
    {
        "Model": "Simple Linear Regression",
        "Implementation": "Without Library",
        "MSE": simple_mse_manual,
        "RMSE": simple_rmse_manual,
        "MAE": simple_mae_manual,
        "R2 Score": simple_r2_manual
    },
    {
        "Model": "Multiple Linear Regression",
        "Implementation": "With Library",
        "MSE": multiple_mse_lib,
        "RMSE": multiple_rmse_lib,
        "MAE": multiple_mae_lib,
        "R2 Score": multiple_r2_lib
    },
    {
        "Model": "Multiple Linear Regression",
        "Implementation": "Without Library",
        "MSE": multiple_mse_manual,
        "RMSE": multiple_rmse_manual,
        "MAE": multiple_mae_manual,
        "R2 Score": multiple_r2_manual
    },
    {
        "Model": "Polynomial Regression",
        "Implementation": "With Library",
        "MSE": poly_mse_lib,
        "RMSE": poly_rmse_lib,
        "MAE": poly_mae_lib,
        "R2 Score": poly_r2_lib
    },
    {
        "Model": "Polynomial Regression",
        "Implementation": "Without Library",
        "MSE": poly_mse_manual,
        "RMSE": poly_rmse_manual,
        "MAE": poly_mae_manual,
        "R2 Score": poly_r2_manual
    }
])

print(final_results.round(4))



# Use the library-based models for model-to-model comparison
model_names = [
    "Simple Linear",
    "Multiple Linear",
    "Polynomial"
]

model_mse = [simple_mse_lib, multiple_mse_lib, poly_mse_lib]
model_rmse = [simple_rmse_lib, multiple_rmse_lib, poly_rmse_lib]
model_mae = [simple_mae_lib, multiple_mae_lib, poly_mae_lib]
model_r2 = [simple_r2_lib, multiple_r2_lib, poly_r2_lib]

# Compare error metrics
x = np.arange(len(model_names))
width = 0.25

plt.figure(figsize=(10, 5))
plt.bar(x - width, model_mse, width, label="MSE")
plt.bar(x, model_rmse, width, label="RMSE")
plt.bar(x + width, model_mae, width, label="MAE")

plt.xticks(x, model_names)
plt.ylabel("Metric Value")
plt.title("Comparison of Regression Models: Error Metrics")
plt.legend()
plt.tight_layout()
plt.show()

# Compare R2 scores separately
plt.figure(figsize=(8, 5))
plt.bar(model_names, model_r2)
plt.axhline(0, color="black", linewidth=0.8)

plt.ylabel("R2 Score")
plt.title("Comparison of Regression Models: R2 Score")
plt.tight_layout()
plt.show()



# Compare library-based models using test-set RMSE
best_index = int(np.argmin(model_rmse))
best_model = model_names[best_index]

print("FINAL MODEL COMPARISON")
print("----------------------")
print("Best model by test RMSE:", best_model)
print("RMSE:", model_rmse[best_index])
print("MAE:", model_mae[best_index])
print("R2 Score:", model_r2[best_index])

print("\nInterpretation:")
print("Lower RMSE and MAE indicate lower prediction errors.")
print("A higher R2 score generally indicates a better fit.")
print("Use the test-set results to compare the models.")
