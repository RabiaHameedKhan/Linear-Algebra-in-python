import numpy as np

# Function to perform row operations and find the inverse
def inverse_by_row_operations(A):
    n = len(A)
    
    # Augment A with the identity matrix (A | I)
    augmented_matrix = np.hstack((A, np.identity(n, dtype=float)))

    # Apply Gauss-Jordan Elimination
    for i in range(n):
        # Make the diagonal element 1
        if augmented_matrix[i, i] == 0:
            for j in range(i + 1, n):
                if augmented_matrix[j, i] != 0:
                    augmented_matrix[[i, j]] = augmented_matrix[[j, i]]  # Swap rows
                    break
            else:
                return "Matrix is singular (non-invertible)."

        augmented_matrix[i] /= augmented_matrix[i, i]

        # Make other elements in column i zero
        for j in range(n):
            if i != j:
                augmented_matrix[j] -= augmented_matrix[j, i] * augmented_matrix[i]

    # Extract the inverse from the augmented matrix
    inverse_matrix = augmented_matrix[:, n:]
    return inverse_matrix

# Function to input the matrix
def input_matrix():
    n = int(input("Enter the order (n x n) of the matrix: "))
    A = []

    print(f"Enter the {n}x{n} matrix row by row:")
    for i in range(n):
        row = list(map(float, input(f"Enter row {i+1} (separated by spaces): ").split()))
        
        while len(row) != n:
            print(f"Error: Please enter exactly {n} numbers.")
            row = list(map(float, input(f"Re-enter row {i+1}: ").split()))
        
        A.append(row)

    return np.array(A, dtype=float)

# Main function
def main():
    A = input_matrix()
    
    # Calculate inverse using row operations
    result = inverse_by_row_operations(A)
    
    # Output the result
    if isinstance(result, str):
        print("\n" + result)
    else:
        print("\nThe inverse of the matrix is:")
        print(result)

# Run the program
if __name__ == "__main__":
    main()
