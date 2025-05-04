import numpy as np

def gaussian_elimination(matrix):
    matrix = matrix.astype(float)
    rows, cols = matrix.shape

    for i in range(min(rows, cols)):
        # Pivoting: Find the row with the largest absolute value in column i
        max_row = i + np.argmax(np.abs(matrix[i:, i]))
        
        # Swap rows if necessary
        if matrix[max_row, i] == 0:
            continue  # Skip if pivot element is zero
        
        matrix[[i, max_row]] = matrix[[max_row, i]]  # Swap rows

        # Make the pivot element 1
        matrix[i] = matrix[i] / matrix[i, i]

        # Eliminate below
        for j in range(i+1, rows):
            matrix[j] -= matrix[j, i] * matrix[i]
    
    return matrix

def calculate_rank_and_nullity(matrix):
    matrix = gaussian_elimination(matrix)  # Perform Gaussian Elimination to get row echelon form
    rank = 0

    # Count non-zero rows in the row echelon form (rows with non-zero leading elements)
    for i in range(matrix.shape[0]):
        if np.any(np.abs(matrix[i]) > 1e-10):  # Tolerance for floating-point errors
            rank += 1
    
    nullity = matrix.shape[1] - rank  # Nullity = columns - rank

    return rank, nullity

def main():
    # Input the matrix dimensions and matrix elements
    rows = int(input("Enter the number of rows in the matrix: "))
    cols = int(input("Enter the number of columns in the matrix: "))
    
    # Input the matrix elements
    matrix = []
    print(f"Enter the matrix elements row by row (separated by commas):")
    for i in range(rows):
        row = list(map(float, input(f"Enter row {i+1}: ").split(',')))
        if len(row) != cols:
            print("Error: Row length does not match number of columns.")
            return
        matrix.append(row)
    
    # Convert the list of lists into a numpy array
    matrix = np.array(matrix)

    # Calculate rank and nullity
    rank, nullity = calculate_rank_and_nullity(matrix)
    
    # Display the result
    print(f"\nRank of the matrix: {rank}")
    print(f"Nullity of the matrix: {nullity}")

# Run the main function
if __name__ == "__main__":
    main()
