## 📌 Quick Revision Notes – Linear Regression

### 🔹 Axis in Pandas
- **axis = 0 → Rows**
- **axis = 1 → Columns**

### 🔹 Train and Test Split Ratio
- If dataset is **small → 80 / 20**
- If dataset is **large → 90 / 10**

### 🔹 Overfitting
- **Training error ↓**
- **Testing error ↑**
- Model memorizes training data but fails on new data

### 🔹 Important Rule for train_test_split()
It always returns in this exact order:
- **X_train**
- **X_test**
- **y_train**
- **y_test**
⚠ **Never change the left-side order while assigning**

### 🔹 random_state
- Fixes randomness
- Same training and testing rows every time
- Gives stable comparison

## 📊 Evaluation Metrics

### 🔹 MAE (Mean Absolute Error)
- **Average mistake**
- Same unit as output

### 🔹 MSE (Mean Squared Error)
- **Squared punishment**
- Large errors heavily penalized

### 🔹 R² Score
- **Overall fit quality**
- Measures how much variation model explains

**R² Meaning:**
- **1 → Perfect**
- **0 → Useless**
- **Negative → Worse than average**

Example:  
If **R² = 0.85 → Model explains 85% of variation in data**  
Higher **R² → Better model fit**

### 🔹 Adjusted R²
- Prevents fake improvement
- Penalizes unnecessary features  
If **R² increases but Adjusted R² drops → New feature is useless**

## 📈 Other Important Regression Metrics
- **MAE → Average error**
- **MSE → Squared punishment**
- **RMSE → Practical error measure**
- **R² → Model strength**
- **Adjusted R² → Fair model strength**
- **MAPE → Percentage error**
- **Median Absolute Error → Robust to outliers**

## 📂 Dataset Handling

### 🔹 train_test_split()
- Splits single dataset into:
  - **Training data**
  - **Testing data**
- No need separate **train.csv** and **test.csv** for small projects