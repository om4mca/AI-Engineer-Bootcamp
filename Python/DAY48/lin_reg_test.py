import numpy as np

X = np.array([
    [1, 1],
    [1, 2],
    [1, 3]
])

y = np.array([2, 4, 5])

weights, residuals, rank, singular_values = np.linalg.lstsq(
    X,
    y,
    rcond=None
)

print("Weights:", weights)
print("Residuals:", residuals)
print("Rank:", rank)

predictions = X @ weights

print(predictions)

print("Actual:", y)
print("Predicted:", predictions)

residuals = y - predictions

print("Residuals:", residuals)

squared_errors = residuals ** 2

print(squared_errors)

rss = np.sum(squared_errors)

print("RSS:", rss)


mse = np.mean((y - predictions) ** 2)

print("MSE:", mse)

