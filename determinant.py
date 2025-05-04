import numpy as np

def get_matrix(n, name="Matrix"):
    """Function to take a square matrix (n x n) input from the user."""
    print(f"\nEnter elements for {name} ({n}x{n}):")
    matrix = []
    for i in range(n):
        row = list(map(float, input(f"Row {i+1}: ").split()))
        if len(row) != n:
            print(f"Error: Please enter exactly {n} values.")
            return get_matrix(n, name)
        matrix.append(row)
    return np.array(matrix)

def calculate_determinant():
    """Function to calculate the determinant of a square matrix."""
    n = int(input("Enter the order (n x n) of the matrix: "))
    A = get_matrix(n, "Matrix A")

    det = np.linalg.det(A)
    
    print("\nMatrix A:")
    print(A)
    print(f"\nDeterminant of the matrix: {round(det, 4)}")  # Rounded for readability

# Run the function
if __name__ == "__main__":
    calculate_determinant()
