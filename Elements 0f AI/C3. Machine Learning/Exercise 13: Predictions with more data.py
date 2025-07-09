import numpy as np
from io import StringIO

input_string = '''
25 2 50 1 500 127900
39 3 10 1 1000 222100
13 2 13 1 1000 143750
82 5 20 2 120 268000
130 6 10 2 600 460700
115 6 10 1 550 407000
'''

np.set_printoptions(precision=1)

def fit_model(input_file):
    data = np.genfromtxt(input_file)

    X = data[:, :5]   # Take first 5 columns as features
    y = data[:, 5]    # Last column is target

    # Fit linear regression WITHOUT intercept (matches test case)
    c = np.linalg.lstsq(X, y, rcond=None)[0]

    # Predictions
    y_pred = X @ c

    print(c)
    print(y_pred)

# Simulate reading a file
input_file = StringIO(input_string)
fit_model(input_file)
