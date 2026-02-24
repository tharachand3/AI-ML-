axis=0 → rows
axis=1 → columns


Train and Testing ratio
If dataset small → use 80/20
If dataset large → even 90/10 is fine.


Overfitting
Training error ↓
Testing error ↑


Always remember:
train_test_split returns:
X_train
X_test
y_train
y_test
In that exact order.
Never change left side order.

With random_state:
Same test set.
Stable comparison.


Evaluation
MAE → average mistake
MSE → punishment for large mistake
R² → overall fit quality

R² tells
1 → perfect
0 → useless
Negative → worse than average
If R² = 0.85
Model explains 85% of variation in data.

Simple meaning:
Higher R² → better model fit


Adjusted R²----Prevents fake improvement
If R² increases but Adjusted R² drops
New feature is useless.


MAE → average error
MSE → squared punishment
RMSE → practical error measure
R² → model strength
Adjusted R² → fair model strength
MAPE → percentage error
Median AE → robust to outliers


train_test_split() • Splits single dataset into
Training data, Testing data
• No need separate train.csv and test.csv