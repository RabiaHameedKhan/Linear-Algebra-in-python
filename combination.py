import numpy as np

def gaussian_elimination(matrix):
    matrix = matrix.astype(float)
    rows, cols = matrix.shape

    for i in range(min(rows, cols-1)):
        # Pivot
        max_row = i + np.argmax(np.abs(matrix[i:, i]))
        if matrix[max_row, i] == 0:
            continue
        matrix[[i, max_row]] = matrix[[max_row, i]]

        # Make leading 1
        matrix[i] = matrix[i] / matrix[i, i]

        # Eliminate below
        for j in range(i+1, rows):
            matrix[j] = matrix[j] - matrix[j, i] * matrix[i]

    return matrix

def back_substitution(matrix):
    rows, cols = matrix.shape
    unknowns = cols - 1
    solution = np.zeros(unknowns)

    for i in range(unknowns-1, -1, -1):
        s = matrix[i, -1]
        for j in range(i+1, unknowns):
            s -= matrix[i, j] * solution[j]
        if matrix[i, i] != 0:
            solution[i] = s / matrix[i, i]
        else:
            solution[i] = 0  # Free variable if no pivot

    return solution

def solve_linear_combination():
    n = int(input("Enter the number of vectors (excluding W): "))
    size = int(input("Enter the dimension of the vectors: "))

    W = np.array(list(map(float, input("Enter vector W (comma-separated): ").split(','))))
    if len(W) != size:
        print("Error: W must have the same dimension.")
        return

    vectors = []

    for i in range(n):
        vector = np.array(list(map(float, input(f"Enter vector U{i+1} (comma-separated): ").split(','))))
        if len(vector) != size:
            print("Error: All vectors must have the same dimension.")
            return
        vectors.append(vector)

    vectors = np.array(vectors).T  # Each column is Ui

    print("\nFormed matrix (each column is a Ui vector):")
    print(vectors)

    # Build augmented matrix [U1 U2 ... Un | W]
    augmented_matrix = np.hstack((vectors, W.reshape(-1, 1)))

    print("\nApplying Gaussian Elimination...")
    reduced_matrix = gaussian_elimination(augmented_matrix.copy())
    print("Row-Echelon Form:")
    print(np.round(reduced_matrix, 2))

    print("\nFinding solution (k1, k2, ..., kn):")
    solution = back_substitution(reduced_matrix)

    for idx, val in enumerate(solution):
        print(f"k{idx+1} = {val}")

    # Spanning Test: Calculate the determinant of the matrix formed by vectors
    det = np.linalg.det(vectors)
    if np.isclose(det, 0):
        print("\nSpanning not Possible.")
    else:
        print("\nSpanning is possible.")

        # Linear Independence Test: If the determinant is non-zero, the vectors are linearly independent
        if not np.isclose(det, 0):
            print("\nThe vectors are linearly independent.")
            print("\nBasis can be formed.")

# Run the function
solve_linear_combination()
