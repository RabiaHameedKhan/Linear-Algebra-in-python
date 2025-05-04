import numpy as np

def solve_network_flow():
    # Coefficients of the linear system (A matrix)
    A = np.array([
        [1, 1, 0],  # x1 + x3 = 30  (Node A)
        [0, 1, 1],  # x2 + x3 = 35  (Node B)
        [0, 0, 1]   # x3 = 45        (Node C)
    ], dtype=float)

    # Right-hand side constants (B matrix)
    B = np.array([30, 35, 45], dtype=float)

    # Solve for x1, x2, x3 using numpy.linalg.solve
    solution = np.linalg.solve(A, B)

    # Display the results
    print("\nSolution for flow rates:")
    for i, val in enumerate(solution, 1):
        print(f"x{i} = {val:.2f}")

    # Interpret negative values
    if solution[1] < 0:
        print("\nNote: x2 is negative, meaning the assumed direction is incorrect.")

# Run the function
solve_network_flow()
