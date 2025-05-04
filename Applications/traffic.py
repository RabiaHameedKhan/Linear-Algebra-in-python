import numpy as np

def solve_traffic_flow():
    # Corrected coefficient matrix (A) - Now it's a 6x6 square matrix
    A = np.array([
        [1, -1,  0,  0,  0,  0],  # x1 - x2 = -100 (Node A)
        [0,  1, -1,  0, -1,  0],  # x2 - x3 - x5 = -700 (Node B)
        [0,  0,  1, -1,  0,  0],  # x3 - x4 = 300 (Node C)
        [0,  0,  0,  1,  1, -1],  # x5 + x4 - x6 = 600 (Node D)
        [0,  0,  0,  0,  0,  1],  # x6 = 400 (Node E)
        [1,  0,  0, -1,  0,  0]   # x1 - x4 = 100 (Fixed equation)
    ], dtype=float)

    # Right-hand side constants (B matrix)
    B = np.array([-100, -700, 300, 600, 400, 100], dtype=float)

    # Solve the system of equations
    solution = np.linalg.solve(A, B)

    # Display the results
    print("\nSolution for traffic flow rates:")
    for i, val in enumerate(solution, 1):
        print(f"x{i} = {val:.2f} vehicles/hour")

# Run the function
solve_traffic_flow()
