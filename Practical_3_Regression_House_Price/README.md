# Practical 3: House Price Prediction Using Regression Models

**Course:** Artificial Intelligence & Machine Learning (Continuous Assessment)  
**Author:** Shruti Siddheshwar Thorat  
**Batch:** A1 | **Roll No:** 16 | **PRN:** 202401040053  

---

## 📌 Aim & Objectives
To implement and compare **Simple Linear Regression**, **Multiple Linear Regression**, and **Polynomial Regression** (degree 2) using both **library-based (Scikit-learn)** and **from-scratch manual mathematical approaches** (Least Squares & Gradient Descent) on the Housing dataset.

---

## 🔬 Dataset & Preprocessing
- **Source:** Housing Price Prediction Dataset (`Housing.csv`, 545 rows $\times$ 13 columns).
- **Features Selected:** `area`, `bedrooms`, `bathrooms`, `stories`, `parking`.
- **Target:** `price`.
- **Cleaning:** Deduplication, null value imputation using median, numeric casting, positive price/area enforcement.
- **Split:** 80% Training (436 rows), 20% Testing (109 rows) with `random_state=42`.

---

## 📐 Mathematical Formulation & Models

### 1. Simple Linear Regression ($Y = mX + c$)
- **Library:** `sklearn.linear_model.LinearRegression`
- **Manual Implementation:** Closed-form **Ordinary Least Squares (OLS)**:
  $$m = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2}, \quad c = \bar{y} - m\bar{x}$$

### 2. Multiple Linear Regression ($Y = b_0 + b_1X_1 + \dots + b_nX_n$)
- **Library:** `sklearn.linear_model.LinearRegression`
- **Manual Implementation:** Standardized **Gradient Descent Optimization**:
  $$\text{weights} \leftarrow \text{weights} - \alpha \cdot \frac{2}{n} X^T (Xw - y)$$
  *(Learning rate $\alpha = 0.03$, $10000$ iterations, features scaled via z-score)*

### 3. Polynomial Regression (Degree 2: $Y = b_0 + b_1X + b_2X^2$)
- **Library:** `PolynomialFeatures(degree=2)` + `LinearRegression`
- **Manual Implementation:** Vandermonde design matrix $[1, Z, Z^2]$ solved via NumPy least-squares `np.linalg.lstsq`.

---

## 📊 Comprehensive Model Benchmarking

| Model | Approach | MSE | RMSE | MAE | $R^2$ Score |
|---|---|---|---|---|---|
| **Simple Linear Regression** | With Library | $3.6753 \times 10^{12}$ | $1,917,104$ | $1,474,748$ | **0.2729** |
| **Simple Linear Regression** | Without Library | $3.6753 \times 10^{12}$ | $1,917,104$ | $1,474,748$ | **0.2729** |
| **Multiple Linear Regression** | With Library | $2.2927 \times 10^{12}$ | $1,514,174$ | $1,127,483$ | **0.5464** |
| **Multiple Linear Regression** | Without Library (GD) | $2.2927 \times 10^{12}$ | $1,514,174$ | $1,127,483$ | **0.5464** |
| **Polynomial Regression** | With Library | $3.5620 \times 10^{12}$ | $1,887,327$ | $1,435,043$ | **0.2953** |
| **Polynomial Regression** | Without Library | $3.5620 \times 10^{12}$ | $1,887,327$ | $1,435,043$ | **0.2953** |

### 🏆 Key Insights
1. **Best Performing Model:** **Multiple Linear Regression** achieved the highest accuracy ($R^2 \approx 0.5464$) and lowest error ($\text{RMSE} \approx 1.514 \times 10^6$), demonstrating that multi-attribute property features provide far more predictive power than area alone.
2. **Mathematical Equivalence:** The manual from-scratch mathematical implementations (Least Squares and Gradient Descent) matched Scikit-learn's library outputs down to double-precision tolerances.

---

## 🚀 Execution Instructions

### Run Jupyter Notebook
```bash
jupyter notebook Practical_3_House_Price_Prediction.ipynb
```

### Run Python Script
```bash
python house_price_prediction.py
```
