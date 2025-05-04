import numpy as np

# Coefficients matrix (A)
A = np.array([
    [1, 1, -1],  # I1 + I2 - I5 = 0
    [5, 0, 20],  # 5I1 + 20I3 = 50
    [0, 10, 20]  # 10I2 + 20I3 = 30
], dtype=float)

# Constants matrix (B)
B = np.array([0, 50, 30], dtype=float)

# Solve for I1, I2, I3
solution = np.linalg.solve(A, B)

# Display results
I1, I2, I3 = solution
print(f"I1 = {I1:.2f} A")
print(f"I2 = {I2:.2f} A")
print(f"I3 = {I3:.2f} A")
